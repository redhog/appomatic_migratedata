appomatic_migratedata
=====================

Copies model data from a one database to another. Basically shortcutting a dumpdata > file.json; loaddata file.json if both destination and source database are online.

This significantly reduces the disksace needed by the process, but also significantly reduces the RAM needed.
