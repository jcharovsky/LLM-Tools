#!/usr/bin/env python3
"""
Markdown Scraper - Scrapes HTML content and converts to Markdown from all sub-URLs
"""

import argparse
import os
import sys
import re
import subprocess
from urllib.parse import urljoin, urlparse

# Auto-install dependencies if missing
def install_requirements():
    """Install required packages if not already installed"""
    required_packages = {
        'requests': 'requests',
        'bs4': 'beautifulsoup4',
        'html2text': 'html2text'
    }

    missing_packages = []
    for import_name, package_name in required_packages.items():
        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(package_name)

    if missing_packages:
        print(f"Installing missing dependencies: {', '.join(missing_packages)}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
        print("Dependencies installed successfully!\n")

# Install requirements before importing
install_requirements()

import requests
from bs4 import BeautifulSoup
import html2text


def get_all_links(url):
    """Extract all links from a webpage"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        links = set()
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(url, link['href'])
            links.add(absolute_url)

        return links
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return set()


def get_domain_name(url):
    """Extract the main domain name from URL (e.g., 'brightdata' from 'https://docs.brightdata.com')"""
    parsed = urlparse(url)
    domain = parsed.netloc

    # Remove port if present
    domain = domain.split(':')[0]

    # Split by dots
    parts = domain.split('.')

    # Remove common subdomains (www, docs, api, etc.) and get the main domain
    # If we have something like docs.brightdata.com, we want 'brightdata'
    # If we have brightdata.com, we want 'brightdata'
    if len(parts) >= 2:
        # Get the second-to-last part (the main domain before the TLD)
        domain_name = parts[-2]
    else:
        domain_name = parts[0]

    return domain_name


def get_filename_from_url(url):
    """Extract filename from the last segment of URL path"""
    parsed = urlparse(url)
    path = parsed.path.strip('/')

    # Get the last segment of the path
    if '/' in path:
        filename = path.split('/')[-1]
    else:
        filename = path

    # If empty, use 'index'
    if not filename:
        filename = 'index'

    # Remove any file extensions that might be in the URL
    filename = re.sub(r'\.(html|htm|php|asp|aspx)$', '', filename, flags=re.IGNORECASE)

    # Sanitize the filename (remove special characters)
    filename = re.sub(r'[^\w\-]', '_', filename)

    # Limit filename length
    if len(filename) > 200:
        filename = filename[:200]

    return filename or 'page'


def convert_html_to_markdown(html_content):
    """Convert HTML content to Markdown format"""
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove unwanted elements
    for element in soup(['script', 'style', 'nav', 'footer', 'header', 'iframe', 'noscript']):
        element.decompose()

    # Get the cleaned HTML
    cleaned_html = str(soup)

    # Configure html2text
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap text
    h.single_line_break = False

    # Convert to markdown
    markdown = h.handle(cleaned_html)

    return markdown.strip()


def scrape_url(url, output_dir):
    """Scrape HTML content and convert to Markdown"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Check if it's HTML content
        content_type = response.headers.get('content-type', '').lower()
        if 'html' not in content_type:
            print(f"⊘ Skipped (not HTML): {url}")
            return False

        # Convert HTML to Markdown
        markdown_content = convert_html_to_markdown(response.content)

        if not markdown_content.strip():
            print(f"⊘ Skipped (no content): {url}")
            return False

        # Create filename from URL path
        filename = get_filename_from_url(url) + '.md'
        filepath = os.path.join(output_dir, filename)

        # Handle duplicate filenames
        counter = 1
        original_filepath = filepath
        while os.path.exists(filepath):
            name, ext = os.path.splitext(original_filepath)
            filepath = f"{name}_{counter}{ext}"
            counter += 1

        # Save markdown content with URL metadata
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {get_filename_from_url(url)}\n\n")
            f.write(f"**Source URL:** {url}\n\n")
            f.write("---\n\n")
            f.write(markdown_content)

        print(f"✓ Scraped: {url} -> {os.path.basename(filepath)}")
        return True
    except Exception as e:
        print(f"✗ Failed to scrape {url}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Scrape HTML content and convert to Markdown from all sub-URLs'
    )
    parser.add_argument('url', help='The URL to scrape content from')
    parser.add_argument(
        '-o', '--output',
        default=None,
        help='Output directory for markdown files (default: domain name from URL)'
    )
    parser.add_argument(
        '--all-domains',
        action='store_true',
        help='Scrape URLs from all domains (default: same domain only)'
    )

    args = parser.parse_args()

    # Set output directory to domain name if not specified
    if args.output is None:
        args.output = get_domain_name(args.url)

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    print(f"Fetching links from: {args.url}")
    links = get_all_links(args.url)

    if not links:
        print("No links found!")
        return

    # Filter by domain (default behavior, unless --all-domains is specified)
    if not args.all_domains:
        base_domain = urlparse(args.url).netloc
        links = {link for link in links if urlparse(link).netloc == base_domain}
        print(f"Filtering to same domain only: {base_domain}")

    print(f"\nFound {len(links)} links to scrape")
    print(f"Saving to: {args.output}/\n")

    # Scrape all links
    successful = 0
    for i, link in enumerate(links, 1):
        print(f"[{i}/{len(links)}] ", end='')
        if scrape_url(link, args.output):
            successful += 1

    print(f"\n{'='*60}")
    print(f"Scraped {successful}/{len(links)} pages successfully")
    print(f"Files saved to: {os.path.abspath(args.output)}")


if __name__ == '__main__':
    main()