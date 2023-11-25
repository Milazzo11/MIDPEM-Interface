MIDPEM "all" command interface for distributed systems with a large number of devices.
This script uses program delays in MIDEPM command execution to ensure Discord rate-limiting does not occur.

FORMAT:
$cmd %s <args> —————— additional arguments
^     |______________ "%s" indicates where device identifier will be inserted
command

EXAMPLE:
$gf %s benchmark.txt