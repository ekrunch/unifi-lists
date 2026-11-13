# unifi-lists
Parsed lists for use in Unifi Network Application 11's Dynamic Network lists feature. This feature currently doesn't support comments in the input files so they have to be parsed beforehand. This repo contains the actions and scripts used to parsed various source lists and the resulting output, for use in UNA 11.

# WARNING
Please do not point your Unifi device at my repo. Why? Because if I ever stop maintaining it, your device might not work or get updated properly, which can create a security issue on your network. Use this repository as an example of what needs to be done to make the device work properly with dynamic lists.

### Current Lists
[DoH Server Lists](DoH/) - These lists are from the [DoH-IP-blocklists]https://github.com/dibdot/DoH-IP-blocklists repository. The only change is the removal of the comments and whitespace, as the Unifi Network Application doesn't parse the comments. My use case for this is to create an outbound network rule to block access to DoH servers so that devices cannot go around the specified DNS servers.
