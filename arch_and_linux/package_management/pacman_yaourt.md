
### yaourt skip pgp sig check

https://github.com/archlinuxfr/yaourt/issues/108
yaourt --m-arg "--skipchecksums --skippgpcheck" -Sb package

### Find files not tracked by package system
`LC_ALL=C find "/usr/lib/perl5/core_perl" -type f -exec pacman -Qqo {} + |& sed -n 's/^error: No package owns \(.*\)$/\1/p'`

From an warning when update the system:
```
( 4/17) Warn about old perl modules
error: No package owns /usr/lib/perl5/core_perl
WARNING: 242 file(s) in /usr/lib/perl5/core_perl are not tracked by pacman and need to be rebuilt.
 -> These were most likely installed directly by cpan or a similar tool.
    Run the following command to get a list of these files:
    LC_ALL=C find "/usr/lib/perl5/core_perl" -type f -exec pacman -Qqo {} + |& sed -n 's/^error: No package owns \(.*\)$/\1/p'
error: No package owns /usr/lib/perl5/vendor_perl
WARNING: 66 file(s) in /usr/lib/perl5/vendor_perl are not tracked by pacman and need to be rebuilt.
 -> These were most likely installed directly by cpan or a similar tool.
    Run the following command to get a list of these files:
    LC_ALL=C find "/usr/lib/perl5/vendor_perl" -type f -exec pacman -Qqo {} + |& sed -n 's/^error: No package owns \(.*\)$/\1/p'
```
