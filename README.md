# unifi-lists
Parsed lists for use in Unifi Network Application 11 and it's Dynamic Network Lists feature. This feature currently doesn't support comments in the input files so they to be parsed beforehand. This repository hosts copies of the lists after parsing them with actions. All actions/scripts are in this repo.

### Current Lists
[DoH Server Lists](DoH/) - These lists are from the [DoH-IP-blocklists]https://github.com/dibdot/DoH-IP-blocklists repository. The only change is the removal of the comments and whitespace, as the Unifi Network Application doesn't parse the comments. My use case for this is to create an outbound network rule to block access to DoH servers so that devices cannot go around the specified DNS servers.
