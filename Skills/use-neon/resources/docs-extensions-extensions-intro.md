# extensions-extensions-intro

**Source URL:** https://neon.com/docs/extensions/extensions-intro

---

[We’re funding open source projects built on Postgres. Learn more![](/_next/static/svgs/9ee958f8b2be7694e4ce9140c14df68e.svg)](https://neon.com/programs/open-source)

Search...

Ask AI

[](/docs)/Extensions

# Postgres extensions

Explore supported Postgres extensions by category. Also see:

  * [List view](/docs/extensions/pg-extensions)
  * [Install an extension](/docs/extensions/pg-extensions#install-an-extension)
  * [Update an extension](/docs/extensions/pg-extensions#update-an-extension-version)



**Need an extension we don't have?** 📩 [Request an extension](/docs/extensions/pg-extensions#request-an-extension)

## AI / Machine Learning

  * ### [pg_tiktokenTokenize data in Postgres using the OpenAI tiktoken library](/docs/extensions/pg_tiktoken)
  * ### [pgragCreate end-to-end Retrieval-Augmented Generation (RAG) pipelines](/docs/extensions/pgrag)
  * ### [pgvectorStore vector embeddings and perform vector similarity search in Postgres](/docs/extensions/pgvector)



## Analytics

  * ### [pg_mooncakeAdds columnstore tables and DuckDB execution for fast analytics in Postgres.](/docs/extensions/pg_mooncake)
  * ### [hllImplements a HyperLogLog data structure as a native data type for efficient and tunable distinct value counting](https://github.com/citusdata/postgresql-hll)
  * ### [timescaledbEnables Postgres as a time-series database for efficient storage and retrieval of time-series data](/docs/extensions/timescaledb)



## Auditing / Logging

  * ### [insert_usernameImplements a trigger that stores the current user's name into a text field, useful for tracking who modified a particular row within a table](https://www.postgresql.org/docs/current/contrib-spi.html)
  * ### [moddatetimeImplements a trigger that automatically updates a timestamp column to the current timestamp whenever a row is modified](https://www.postgresql.org/docs/current/contrib-spi.html)
  * ### [pgrowlocksProvides a function that shows row locking information for a specified table, useful in concurrency and deadlock debugging](/docs/extensions/pgrowlocks)
  * ### [tcnProvides a trigger function to notify listeners of changes to a table, allowing applications to respond to changes in the database](https://www.postgresql.org/docs/16/tcn.html)



## Data / Transformations

  * ### [address_standardizerA single-line address parser that takes an input address and normalizes it based on a set of rules](https://postgis.net/docs/Extras.html#Address_Standardizer)
  * ### [address_standardizer_data_usProvides data for standardizing US addresses, for use with the address_standardizer extension](https://postgis.net/docs/Extras.html#Address_Standardizer_Tables)
  * ### [anonProvides data masking and anonymization capabilities for protecting personally identifiable information (PII) and sensitive data in Postgres databases](/docs/extensions/postgresql-anonymizer)
  * ### [citextProvides a case-insensitive character string type that internally calls lower when comparing values in Postgres](/docs/extensions/citext)
  * ### [cubeImplements the cube data type for representing multidimensional cubes in Postgres](/docs/extensions/cube)
  * ### [earthdistanceProvides cube-based and point-based approaches to calculating great circle distances on the surface of the Earth](/docs/extensions/earthdistance)
  * ### [hstoreImplements an hstore data type for storing and manipulating sets of key-value pairs within a single Postgres value](/docs/extensions/hstore)
  * ### [intaggProvides an integer aggregator and enumerator for Postgres](https://www.postgresql.org/docs/16/intagg.html)
  * ### [intarrayOffers functions and operators for manipulating and searching arrays of integers within Postgres](/docs/extensions/intarray)
  * ### [isnImplements data types for international product numbering standards: EAN13, UPC, ISBN (books), ISMN (music), and ISSN (serials)](https://www.postgresql.org/docs/16/isn.html)
  * ### [ltreeProvides data types for representing labels of data stored in a hierarchical tree-like structure and facilities for searching through label trees](/docs/extensions/ltree)
  * ### [pg_graphqlAdds GraphQL support to Postgres, allowing you to query your database via GraphQL](/docs/extensions/pg_graphql)
  * ### [pg_hashidsEnables the generation of short, unique hash ids from integers, useful for obfuscating internal ids](https://github.com/iCyberon/pg_hashids)
  * ### [pg_jsonschemaProvides support for JSON schema validation on json and jsonb data types](https://github.com/supabase/pg_jsonschema)
  * ### [pg_uuidv7Enables creating valid UUID Version 7 values in Postgres, enabling globally unique identifiers with temporal ordering](/docs/extensions/pg_uuidv7)
  * ### [pgx_ulidA full-featured extension for generating and working with ULID (Universally Unique Lexicographically Sortable Identifiers)](https://github.com/pksunkara/pgx_ulid)
  * ### [segImplements the seg data type for storage and manipulation of line segments or floating-point ranges, useful for geometric and scientific applications](https://www.postgresql.org/docs/16/seg.html)
  * ### [semverA Postgres data type for the Semantic Version format with support for btree and hash indexing](https://pgxn.org/dist/semver)
  * ### [tablefuncContains functions that return tables (multiple rows), including crosstab, which can pivot row data into columns dynamically](/docs/extensions/tablefunc)
  * ### [unaccentA text search dictionary that removes accents from characters, simplifying text search in Postgres](/docs/extensions/unaccent)
  * ### [unitImplements a data type for SI units, plus byte, for storage, manipulation, and calculation of scientific units](https://github.com/df7cb/postgresql-unit)
  * ### [uuid-osspProvides functions to generate universally unique identifiers (UUIDs) in Postgres, supporting various UUID standards](/docs/extensions/uuid-ossp)
  * ### [wal2jsonA Postgres logical decoding plugin that converts Write-Ahead Log (WAL) changes into JSON objects](/docs/extensions/wal2json)
  * ### [xml2Enables XPath queries and XSLT functionality directly within Postgres, enabling XML data processing](/docs/extensions/xml2)



## Debugging

  * ### [moddatetimeAutomatically updates a timestamp column to the current timestamp whenever a row is modified in Postgres](https://www.postgresql.org/docs/current/contrib-spi.html)
  * ### [pgrowlocksProvides a function that shows row locking information for a specified table, which can aid in concurrency and deadlock debugging](/docs/extensions/pgrowlocks)
  * ### [pgTapA unit testing framework for Postgres, enabling sophisticated testing of database queries and functions](https://pgtap.org/documentation.html)
  * ### [plpgsql_checkProvides a linter and debugger for PL/pgSQL code, helping identify errors and optimize PL/pgSQL functions](https://pgxn.org/dist/plpgsql_check/)



## Geospatial

  * ### [cubeImplements a data type for representing multidimensional cubes in Postgres](/docs/extensions/cube)
  * ### [earthdistanceProvides cube-based and point-based approaches to calculating great circle distances on the surface of the Earth](/docs/extensions/earthdistance)
  * ### [h3Integrates Uber's H3 geospatial indexing system that combines the benefits of a hexagonal grid with S2's hierarchical subdivisions](/docs/extensions/postgis-related-extensions#h3-and-h3-postgis)
  * ### [h3_postgisA PostGIS extension for H3, enabling advanced spatial analysis and indexing](/docs/extensions/postgis-related-extensions#h3-and-h3-postgis)
  * ### [pgroutingExtends PostGIS/Postgres databases, providing geospatial routing and other network analysis functionality](/docs/extensions/postgis-related-extensions#pgrouting)
  * ### [postgisExtends Postgres to allow GIS (Geographic Information Systems) objects to be stored in the database, enabling spatial queries directly in SQL](/docs/extensions/postgis)
  * ### [postgis_rasterAdds support for raster data to PostGIS, enabling advanced geospatial analysis on raster images](https://postgis.net/docs/RT_reference.html)
  * ### [postgis_sfcgalProvides support for advanced 3D geometries in PostGIS, based on the SFCGAL library](/docs/extensions/postgis-related-extensions#postgis-sfcgal)
  * ### [postgis_tiger_geocoderEnables geocoding and reverse geocoding capabilities in PostGIS using TIGER/Line data](/docs/extensions/postgis-related-extensions#postgis-tiger-geocoder)
  * ### [postgis_topologyExtends PostGIS with support for topological data types and functions, facilitating the analysis of spatial relationships](https://www.postgis.net/docs/Topology.html)



## Index / Table optimization

  * ### [bloomProvides an index access method for Postgres based on Bloom filters](https://www.postgresql.org/docs/16/bloom.html)
  * ### [btree_ginProvides GIN operator classes that implement B-tree equivalent behavior](/docs/extensions/btree_gin)
  * ### [btree_gistProvides GiST index operator classes that implement B-tree equivalent behavior](/docs/extensions/btree_gist)
  * ### [ip4rProvides a range index type and functions for efficiently storing and querying IPv4 and IPv6 ranges and addresses in Postgres](https://github.com/RhodiumToad/ip4r)
  * ### [pg_ivmProvides an Incremental View Maintenance (IVM) feature for Postgres](https://github.com/sraoss/pg_ivm)
  * ### [pg_partmanA partition manager extension that enables creating and managing time-based and number-based table partition sets in Postgres](https://github.com/pgpartman/pg_partman)
  * ### [pg_prewarmAllows manual preloading of relation data into the Postgres buffer cache, reducing access times for frequently queried tables](/docs/extensions/pg_prewarm)
  * ### [pg_repackLets you remove bloat from tables and indexes, and optionally restore the physical order of clustered indexes](/docs/extensions/pg_repack)
  * ### [pg_roaringbitmapImplements Roaring Bitmaps in Postgres for efficient storage and manipulation of bit sets](https://github.com/ChenHuajun/pg_roaringbitmap)
  * ### [rumProvides an access method to work with a RUM index, designed to speed up full-text searches](https://github.com/postgrespro/rum)



## Metrics

  * ### [neonProvides functions and views designed to gather Neon-specific metrics](/docs/extensions/neon)
  * ### [pg_stat_statementsTracks planning and execution statistics for all SQL statements executed, aiding in performance analysis and tuning](/docs/extensions/pg_stat_statements)
  * ### [pgstattupleOffers functions to show tuple-level statistics for tables, helping identify bloat and efficiency opportunities](/docs/extensions/pgstattuple)
  * ### [tsm_system_rowsProvides a table sampling method that selects a fixed number of table rows randomly](https://www.postgresql.org/docs/16/tsm-system-rows.html)
  * ### [tsm_system_timeOffers a table sampling method based on system time, enabling consistent sample data retrieval over time](https://www.postgresql.org/docs/16/tsm-system-time.html)



## Orchestration

  * ### [tcnProvides a trigger function to notify listeners of changes to a table, allowing applications to respond to changes in the database](https://www.postgresql.org/docs/16/tcn.html)
  * ### [pg_partmanA partition manager extension that enables creating and managing time-based and number-based table partition sets in Postgres](https://github.com/pgpartman/pg_partman)



## Procedural languages

  * ### [plcoffeeEnables writing functions in CoffeeScript, a Javascript dialect with a syntax similar to Ruby](https://coffeescript.org/)
  * ### [pllsEnables writing functions in LiveScript, a Javascript dialect that serves as a more powerful successor to CoffeeScript](https://livescript.net/)
  * ### [plv8A Postgres procedural language powered by V8 Javascript Engine for writing functions in Javascript that are callable from SQL](https://github.com/plv8/plv8/)
  * ### [plpgsqlThe default procedural language for Postgres, enabling the creation of complex functions and triggers](https://www.postgresql.org/docs/16/plpgsql.html)



## Query optimization

  * ### [hypopgProvides the ability to create hypothetical (virtual) indexes in Postgres for performance testing](https://hypopg.readthedocs.io/en/rel1_stable/)
  * ### [pg_hint_planAllows developers to influence query plans with hints in SQL comments, improving performance and control over query execution](https://github.com/ossc-db/pg_hint_plan)
  * ### [online_advisorRecommends indexes, extended statistics, and prepared statements based on your actual query workload](/docs/extensions/online_advisor)



## Scientific computing

  * ### [cubeImplements the cube data type for representing multidimensional cubes in Postgres](/docs/extensions/cube)
  * ### [rdkitIntegrates the RDKit cheminformatics toolkit with Postgres, enabling chemical informatics operations directly in the database](https://github.com/rdkit/rdkit)
  * ### [segImplements the seg data type for storage and manipulation of line segments or floating-point intervals, useful for representing laboratory measurements](https://www.postgresql.org/docs/16/seg.html)
  * ### [unitImplements a data type for SI units, plus byte, for storage, manipulation, and calculation of scientific units](https://github.com/df7cb/postgresql-unit)



## Search

  * ### [citextProvides a case-insensitive character string type that internally calls lower when comparing values in Postgres](/docs/extensions/citext)
  * ### [dict_intProvides a text search dictionary template for indexing integer data in Postgres](/docs/extensions/dict_int)
  * ### [fuzzystrmatchProvides several functions to determine similarities and distance between strings in Postgres](/docs/extensions/fuzzystrmatch)
  * ### [pg_searchAn Elasticsearch alternative for full-text search and analytics on Postgres](/docs/extensions/pg_search)
  * ### [pg_trgmProvides functions and operators for determining the similarity of alphanumeric text based on trigram matching, and index operator classes for fast string similarity search](/docs/extensions/pg_trgm)
  * ### [prefixA prefix range module that supports efficient queries on text columns with prefix-based searching and matching capabilities](https://github.com/dimitri/prefix)
  * ### [unaccentA text search dictionary that removes accents from characters, simplifying text search in Postgres](/docs/extensions/unaccent)



## Security

  * ### [anonProvides data masking and anonymization capabilities for protecting personally identifiable information (PII) and sensitive data in Postgres databases](/docs/extensions/postgresql-anonymizer)
  * ### [pg_session_jwtEnables RLS policies to verify user identity directly within SQL queries](/docs/guides/neon-authorize#how-the-pgsessionjwt-extension-works)
  * ### [pgcryptoOffers cryptographic functions, allowing for encryption and hashing of data within Postgres](/docs/extensions/pgcrypto)
  * ### [pgjwtImplements JSON Web Tokens (JWT) in Postgres, allowing for secure token creation and verification](https://github.com/michelp/pgjwt)



## Tooling / Admin

  * ### [autoincProvides an autoinc() function that stores the next value of a sequence into an integer field](https://www.postgresql.org/docs/current/contrib-spi.html)
  * ### [hypopgProvides the ability to create hypothetical (virtual) indexes in Postgres for performance testing](https://hypopg.readthedocs.io/en/rel1_stable/)
  * ### [insert_usernameAutomatically inserts the username of the person executing an insert operation into a specified table in Postgres](https://www.postgresql.org/docs/current/contrib-spi.html)
  * ### [loProvides support for managing large objects (LOBs) in Postgres, including a data type lo and a trigger lo_manage](https://www.postgresql.org/docs/16/lo.html)
  * ### [neon_utilsProvides a function for monitoring how Neon's Autoscaling feature allocates vCPU in response to workload](/docs/extensions/neon-utils)
  * ### [pg_cronLets you schedule and manage periodic jobs directly in your Postgres database](/docs/extensions/pg_cron)
  * ### [pgtapA unit testing framework for Postgres, enabling sophisticated testing of database queries and functions](https://pgtap.org/documentation.html)
  * ### [refintProvides functions for maintaining foreign key constraints](https://www.postgresql.org/docs/current/contrib-spi.html)



## Remote data access

  * ### [dblinkProvides functions for accessing and manipulating data in remote databases from within Postgres](/docs/extensions/dblink)
  * ### [postgres_fdwAccess data in remote Postgres databases as local tables](/docs/extensions/postgres_fdw)



[PreviousAI use in Neon](/docs/security/ai-use-in-neon)[NextSupported extensions](/docs/extensions/pg-extensions)

Last updated on August 15, 2025

Was this page helpful?

YesNo

Thank you for your feedback!

### On this page

  * AI / Machine Learning
  * Analytics
  * Auditing / Logging
  * Data / Transformations
  * Debugging
  * Geospatial
  * Index / Table optimization
  * Metrics
  * Orchestration
  * Procedural languages
  * Query optimization
  * Scientific computing
  * Search
  * Security
  * Tooling / Admin
  * Remote data access



Copy page as markdown[Edit this page on GitHub](https://github.com/neondatabase/website/tree/main/content/docs/extensions/extensions-intro.md)[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https://raw.githubusercontent.com/neondatabase/website/refs/heads/main/content/docs/extensions/extensions-intro.md)

Neon Docs