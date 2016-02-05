### Macros
# Default version 2.27
%{!?upstream_version: %define upstream_version 2.27}
# Default buildnumber to 1
%{!?build_number: %define build_number 1}
%define _prefix /opt/altiscale
%define cytune_archs %{ix86} alpha %{arm}
%define compldir %{_datadir}/bash-completion/completions/

### Header
Summary: A collection of basic system utilities
Name: altiscale-util-linux
Version: %{upstream_version}
Release: %{build_number}%{?dist}
License: GPLv2 and GPLv2+ and LGPLv2+ and BSD with advertising and Public Domain
Group: System Environment/Base
URL: http://en.wikipedia.org/wiki/Util-linux
Prefix: %{_prefix}

### Dependencies
BuildRequires: audit-libs-devel >= 1.0.6
BuildRequires: gettext-devel
BuildRequires: libselinux-devel
BuildRequires: ncurses-devel
BuildRequires: pam-devel
BuildRequires: zlib-devel
BuildRequires: popt-devel
BuildRequires: libutempter-devel
Buildrequires: systemd-devel
Buildrequires: libuser-devel
BuildRequires: libcap-ng-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%define version_dir %(echo %{upstream_version} | %{__awk} -F\. '{ print $1"."$2 }')
### Sources
Source0: ftp://ftp.kernel.org/pub/linux/utils/util-linux/v%{version_dir}/util-linux-%{upstream_version}.tar.xz
#Source1: util-linux-login.pamd
#Source2: util-linux-remote.pamd
#Source3: util-linux-chsh-chfn.pamd
#Source4: util-linux-60-raw.rules
#Source8: nologin.c
#Source9: nologin.8
#Source12: util-linux-su.pamd
#Source13: util-linux-su-l.pamd
#Source14: util-linux-runuser.pamd
#Source15: util-linux-runuser-l.pamd

### Obsoletes & Conflicts & Provides
Conflicts: bash-completion < 1:2.1-1
# su(1) and runuser(1) merged into util-linux v2.22
Conflicts: coreutils < 8.20
# eject has been merged into util-linux v2.22
Obsoletes: eject <= 2.1.5
Provides: eject = 2.1.6
# sulogin, utmpdump merged into util-linux v2.22
#Conflicts: sysvinit-tools < 2.88-8
# old versions of e2fsprogs contain fsck, uuidgen
#Conflicts: e2fsprogs < 1.41.8-5
# rename from util-linux-ng back to util-linux
Obsoletes: altiscale-util-linux-ng < 2.19
Provides: altiscale-util-linux-ng = %{version}-%{release}
Conflicts: filesystem < 3
Provides: /opt/altiscale/bin/dmesg
Provides: /opt/altiscale/bin/kill
Provides: /opt/altiscale/bin/more
Provides: /opt/altiscale/bin/mount
Provides: /opt/altiscale/bin/umount
Provides: /opt/altiscale/sbin/blkid
Provides: /opt/altiscale/sbin/blockdev
Provides: /opt/altiscale/sbin/findfs
Provides: /opt/altiscale/sbin/fsck
Provides: /opt/altiscale/sbin/nologin

Requires(post): coreutils
Requires: altiscale-libuuid = %{version}-%{release}
Requires: altiscale-libblkid = %{version}-%{release}
Requires: altiscale-libmount = %{version}-%{release}

%description
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function. Among
others, Util-linux contains the fdisk configuration tool and the login
program.

%package -n altiscale-libmount
Summary: Device mounting library
Group: Development/Libraries
License: LGPLv2+
Requires: altiscale-libblkid = %{version}-%{release}
Requires: altiscale-libuuid = %{version}-%{release}
Conflicts: filesystem < 3

%description -n altiscale-libmount
This is the device mounting library, part of util-linux.


%package -n altiscale-libmount-devel
Summary: Device mounting library
Group: Development/Libraries
License: LGPLv2+
Requires: altiscale-libmount = %{version}-%{release}
Requires: pkgconfig

%description -n altiscale-libmount-devel
This is the device mounting development library and headers,
part of util-linux.


%package -n altiscale-libblkid
Summary: Block device ID library
Group: Development/Libraries
License: LGPLv2+
Requires: altiscale-libuuid = %{version}-%{release}
Conflicts: filesystem < 3
Requires(post): coreutils

%description -n altiscale-libblkid
This is block device identification library, part of util-linux.


%package -n altiscale-libblkid-devel
Summary: Block device ID library
Group: Development/Libraries
License: LGPLv2+
Requires: altiscale-libblkid = %{version}-%{release}
Requires: pkgconfig

%description -n altiscale-libblkid-devel
This is the block device identification development library and headers,
part of util-linux.


%package -n altiscale-libuuid
Summary: Universally unique ID library
Group: Development/Libraries
License: BSD
Conflicts: filesystem < 3

%description -n altiscale-libuuid
This is the universally unique ID library, part of util-linux.

The libuuid library generates and parses 128-bit universally unique
id's (UUID's).  A UUID is an identifier that is unique across both
space and time, with respect to the space of all UUIDs.  A UUID can
be used for multiple purposes, from tagging objects with an extremely
short lifetime, to reliably identifying very persistent objects
across a network.

See also the "uuid" package, which is a separate implementation.

%package -n altiscale-libuuid-devel
Summary: Universally unique ID library
Group: Development/Libraries
License: BSD
Requires: altiscale-libuuid = %{version}-%{release}
Requires: pkgconfig

%description -n altiscale-libuuid-devel
This is the universally unique ID development library and headers,
part of util-linux.

The libuuid library generates and parses 128-bit universally unique
id's (UUID's).  A UUID is an identifier that is unique across both
space and time, with respect to the space of all UUIDs.  A UUID can
be used for multiple purposes, from tagging objects with an extremely
short lifetime, to reliably identifying very persistent objects
across a network.

See also the "uuid-devel" package, which is a separate implementation.


%package -n altiscale-uuidd
Summary: Helper daemon to guarantee uniqueness of time-based UUIDs
Group: System Environment/Daemons
Requires: altiscale-libuuid = %{version}-%{release}
License: GPLv2
Requires(pre): shadow-utils

%description -n altiscale-uuidd
The uuidd package contains a userspace daemon (uuidd) which guarantees
uniqueness of time-based UUID generation even at very high rates on
SMP systems.


%package -n altiscale-libfdisk
Summary: fdisk libraries
Group: Development/Libraries
License: LGPLv2+
Requires: altiscale-libblkid = %{version}-%{release}
Requires: altiscale-libuuid = %{version}-%{release}
Conflicts: filesystem < 3

%description -n altiscale-libfdisk
This is the fdisk library, part of util-linux.

%package -n altiscale-libfdisk-devel
Summary: fdisk devel
Group: Development/Libraries
License: LGPLv2+
Requires: altiscale-libfdisk = %{version}-%{release}
Requires: pkgconfig

%description -n altiscale-libfdisk-devel
This is the fdisk development library and headers, part of util-linux.

%package -n altiscale-libsmartcols
Summary: smartcols library
Group: Development/Libraries
License: LGPLv2+
Requires: altiscale-libblkid = %{version}-%{release}
Requires: altiscale-libuuid = %{version}-%{release}
Conflicts: filesystem < 3

%description -n altiscale-libsmartcols
This is the smartcols library, part of util-linux.

%package -n altiscale-libsmartcols-devel
Summary: fdisk devel
Group: Development/Libraries
License: LGPLv2+
Requires: altiscale-libsmartcols = %{version}-%{release}
Requires: pkgconfig

%description -n altiscale-libsmartcols-devel
This is the smartcols development library and headers, part of util-linux.

%prep
%setup -q -n util-linux-%{upstream_version}

#cp %{SOURCE8} %{SOURCE9} .

%build
unset LINGUAS || :

# unfortunately, we did changes to build-system
#./autogen.sh

export CFLAGS="-D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 $RPM_OPT_FLAGS"
export SUID_CFLAGS="-fpie"
export SUID_LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"
%configure \
  --without-systemd \
  --without-systemdsystemunitdir \
  --without-audit \
  --without-fdisk \
  --without-smartcols \
  --disable-silent-rules \
  --disable-wall \
  --disable-bfs \
  --disable-pg \
  --enable-socket-activation \
  --enable-chfn-chsh \
  --enable-write \
  --enable-raw \
  --with-udev \
  --with-selinux \
  --with-utempter \
  --disable-makeinstall-chown \
%ifnarch %cytune_archs
  --disable-cytune \
%endif
%ifarch s390 s390x
  --disable-hwclock \
  --disable-fdformat
%endif

# build util-linux
make %{?_smp_mflags}

# build nologin
#gcc $CFLAGS -o nologin nologin.c


%check
#to run tests use "--with check"
%if %{?_with_check:1}%{!?_with_check:0}
make check
%endif


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,6,8,5}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/{pam.d,security/console.apps}
mkdir -p ${RPM_BUILD_ROOT}/var/log
touch ${RPM_BUILD_ROOT}/var/log/lastlog
chmod 0644 ${RPM_BUILD_ROOT}/var/log/lastlog

# install util-linux
make install DESTDIR=${RPM_BUILD_ROOT}

# install nologin
#install -m 755 nologin ${RPM_BUILD_ROOT}%{_sbindir}
#install -m 644 nologin.8 ${RPM_BUILD_ROOT}%{_mandir}/man8

# raw
echo '.so man8/raw.8' > $RPM_BUILD_ROOT%{_mandir}/man8/rawdevices.8
#{
  # see RH bugzilla #216664
#  mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/lib/udev/rules.d
#  pushd ${RPM_BUILD_ROOT}%{_prefix}/lib/udev/rules.d
#  install -m 644 %{SOURCE4} ./60-raw.rules
#  popd
#}

# sbin -> bin
mv ${RPM_BUILD_ROOT}%{_sbindir}/raw ${RPM_BUILD_ROOT}%{_bindir}/raw

# And a dirs uuidd needs that the makefiles don't create
install -d ${RPM_BUILD_ROOT}/run/uuidd
install -d ${RPM_BUILD_ROOT}/var/lib/libuuid

# libtool junk
rm -rf ${RPM_BUILD_ROOT}%{_libdir}/*.la

%ifarch %{sparc}
rm -rf ${RPM_BUILD_ROOT}%{_bindir}/sunhostid
cat << E-O-F > ${RPM_BUILD_ROOT}%{_bindir}/sunhostid
#!/bin/sh
# this should be _bindir/sunhostid or somesuch.
# Copyright 1999 Peter Jones, <pjones@redhat.com> .
# GPL and all that good stuff apply.
(
idprom=\`cat /proc/openprom/idprom\`
echo \$idprom|dd bs=1 skip=2 count=2
echo \$idprom|dd bs=1 skip=27 count=6
echo
) 2>/dev/null
E-O-F
chmod 755 ${RPM_BUILD_ROOT}%{_bindir}/sunhostid
%endif

# PAM settings
#{
#  pushd ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d
#  install -m 644 %{SOURCE1} ./login
#  install -m 644 %{SOURCE2} ./remote
#  install -m 644 %{SOURCE3} ./chsh
#  install -m 644 %{SOURCE3} ./chfn
#  install -m 644 %{SOURCE12} ./su
#  install -m 644 %{SOURCE13} ./su-l
#  install -m 644 %{SOURCE14} ./runuser
#  install -m 644 %{SOURCE15} ./runuser-l
#  popd
#}

%ifnarch s390 s390x
ln -sf hwclock ${RPM_BUILD_ROOT}%{_sbindir}/clock
echo ".so man8/hwclock.8" > ${RPM_BUILD_ROOT}%{_mandir}/man8/clock.8
%endif

# unsupported on SPARCs
%ifarch %{sparc}
for I in /sbin/sfdisk \
  %{_mandir}/man8/sfdisk.8* \
  %doc Documentation/sfdisk.txt \
  /sbin/cfdisk \
  %{_mandir}/man8/cfdisk.8*; do

  rm -f $RPM_BUILD_ROOT$I
done
%endif

# we install getopt-*.{bash,tcsh} as doc files
chmod 644 misc-utils/getopt-*.{bash,tcsh}
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/getopt

ln -sf /proc/mounts %{buildroot}/etc/mtab


# remove static libs
rm -f $RPM_BUILD_ROOT%{_libdir}/lib{uuid,blkid,mount,fdisk,smartcols}.a

# find MO files
%find_lang %name --all-name

# the files section supports only one -f option...
mv %{name}.lang %{name}.files

# create list of setarch(8) symlinks
find  $RPM_BUILD_ROOT%{_bindir}/ -regextype posix-egrep -type l \
  -regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64)$" \
  -printf "%{_bindir}/%f\n" >> %{name}.files

find  $RPM_BUILD_ROOT%{_mandir}/man8 -regextype posix-egrep  \
  -regex ".*(linux32|linux64|s390|s390x|i386|ppc|ppc64|ppc32|sparc|sparc64|sparc32|sparc32bash|mips|mips64|mips32|ia64|x86_64)\.8.*" \
  -printf "%{_mandir}/man8/%f*\n" >> %{name}.files

%post
# only for minimal buildroots without /var/log
[ -d /var/log ] || mkdir -p /var/log
touch /var/log/lastlog
chown root:root /var/log/lastlog
chmod 0644 /var/log/lastlog
# Fix the file context, do not use restorecon
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  SECXT=$( /usr/sbin/matchpathcon -n /var/log/lastlog 2> /dev/null )
  if [ -n "$SECXT" ]; then
    # Selinux enabled, but without policy? It's true for buildroots
    # without selinux stuff on host machine with enabled selinux.
    # We don't want to use any RPM dependence on selinux policy for
    # matchpathcon(2). SELinux policy should be optional.
    /usr/bin/chcon "$SECXT"  /var/log/lastlog >/dev/null 2>&1 || :
  fi
fi
if [ ! -L /etc/mtab ]; then
  ln -fs /proc/mounts /etc/mtab
fi

%post -n altiscale-libblkid
/sbin/ldconfig

### Move blkid cache to /run
[ -d /run/blkid ] || mkdir -p /run/blkid
for I in /etc/blkid.tab /etc/blkid.tab.old \
         /etc/blkid/blkid.tab /etc/blkid/blkid.tab.old; do

  if [ -f "$I" ]; then
    mv "$I" /run/blkid/ || :
  fi
done

%postun -n altiscale-libblkid -p /sbin/ldconfig

%post -n altiscale-libuuid -p /sbin/ldconfig
%postun -n altiscale-libuuid -p /sbin/ldconfig

%post -n altiscale-libmount -p /sbin/ldconfig
%postun -n altiscale-libmount -p /sbin/ldconfig

%post -n altiscale-libfdisk -p /sbin/ldconfig
%postun -n altiscale-libfdisk -p /sbin/ldconfig

%post -n altiscale-libsmartcols -p /sbin/ldconfig
%postun -n altiscale-libsmartcols -p /sbin/ldconfig

%pre -n altiscale-uuidd
getent group uuidd >/dev/null || groupadd -r uuidd
getent passwd uuidd >/dev/null || \
useradd -r -g uuidd -d /var/lib/libuuid -s /sbin/nologin \
    -c "UUID generator helper daemon" uuidd
exit 0

#%post -n altiscale-uuidd
#if [ $1 -eq 1 ]; then
#  # Package install,
#  /bin/systemctl enable uuidd.service >/dev/null 2>&1 || :
#  /bin/systemctl start uuidd.service > /dev/null 2>&1 || :
#else
#  # Package upgrade
#  if /bin/systemctl --quiet is-enabled uuidd.service ; then
#    /bin/systemctl reenable uuidd.service >/dev/null 2>&1 || :
#  fi
#fi

#%preun -n altiscale-uuidd
#if [ "$1" = 0 ]; then
#  /bin/systemctl stop uuidd.service > /dev/null 2>&1 || :
#  /bin/systemctl disable uuidd.service > /dev/null 2>&1 || :
#fi


%files -f %{name}.files
%defattr(-,root,root)
%doc README NEWS AUTHORS
%doc Documentation/deprecated.txt Documentation/licenses/*
%doc misc-utils/getopt-*.{bash,tcsh}

#%config(noreplace)  %{_sysconfdir}/pam.d/chfn
#%config(noreplace)  %{_sysconfdir}/pam.d/chsh
#%config(noreplace)  %{_sysconfdir}/pam.d/login
#%config(noreplace)  %{_sysconfdir}/pam.d/remote
#%config(noreplace)  %{_sysconfdir}/pam.d/su
#%config(noreplace)  %{_sysconfdir}/pam.d/su-l
#%config(noreplace)  %{_sysconfdir}/pam.d/runuser
#%config(noreplace)  %{_sysconfdir}/pam.d/runuser-l
#%config(noreplace)  %{_prefix}/lib/udev/rules.d/60-raw.rules

%attr(4755,root,root) %{_bindir}/mount
%attr(4755,root,root) %{_bindir}/umount
%attr(4755,root,root) %{_bindir}/su
%attr(755,root,root)  %{_bindir}/login
%attr(4711,root,root) %{_bindir}/chfn
%attr(4711,root,root) %{_bindir}/chsh
%attr(2755,root,tty)  %{_bindir}/write

%ghost %attr(0644,root,root) %verify(not md5 size mtime) /var/log/lastlog
%ghost %verify(not md5 size mtime) %config(noreplace,missingok) /etc/mtab

#%{_unitdir}/fstrim.*

/opt/altiscale/share/doc/util-linux/getopt/getopt-parse.bash
/opt/altiscale/share/doc/util-linux/getopt/getopt-parse.tcsh
%{_bindir}/cal
%{_bindir}/chrt
%{_bindir}/col
%{_bindir}/colcrt
%{_bindir}/colrm
%{_bindir}/column
%{_bindir}/dmesg
%{_bindir}/eject
%{_bindir}/fallocate
%{_bindir}/findmnt
%{_bindir}/flock
%{_bindir}/getopt
%{_bindir}/hexdump
%{_bindir}/ionice
%{_bindir}/ipcmk
%{_bindir}/ipcrm
%{_bindir}/ipcs
%{_bindir}/isosize
%{_bindir}/kill
%{_bindir}/last
%{_bindir}/lastb
%{_bindir}/logger
%{_bindir}/look
%{_bindir}/lsblk
%{_bindir}/lscpu
%{_bindir}/lslocks
%{_bindir}/lslogins
%{_bindir}/lsipc
%{_bindir}/mcookie
%{_bindir}/more
%{_bindir}/mountpoint
%{_bindir}/mesg
%{_bindir}/namei
#%{_bindir}/nsenter
%{_bindir}/prlimit
%{_bindir}/raw
%{_bindir}/rename
%{_bindir}/renice
%{_bindir}/rev
%{_bindir}/script
%{_bindir}/scriptreplay
%{_bindir}/setarch
#%{_bindir}/setpriv
%{_bindir}/setsid
%{_bindir}/setterm
%{_bindir}/tailf
%{_bindir}/taskset
%{_bindir}/ul
%{_bindir}/uname26
%{_bindir}/unshare
%{_bindir}/utmpdump
%{_bindir}/uuidgen
%{_bindir}/wdctl
%{_bindir}/whereis
%{_mandir}/man1/cal.1*
%{_mandir}/man1/chfn.1*
%{_mandir}/man1/chrt.1*
%{_mandir}/man1/chsh.1*
%{_mandir}/man1/col.1*
%{_mandir}/man1/colcrt.1*
%{_mandir}/man1/colrm.1*
%{_mandir}/man1/column.1*
%{_mandir}/man1/dmesg.1*
%{_mandir}/man1/eject.1*
%{_mandir}/man1/fallocate.1*
%{_mandir}/man1/flock.1*
%{_mandir}/man1/getopt.1*
%{_mandir}/man1/hexdump.1*
%{_mandir}/man1/ionice.1*
%{_mandir}/man1/ipcmk.1*
%{_mandir}/man1/ipcrm.1*
%{_mandir}/man1/ipcs.1*
%{_mandir}/man1/kill.1*
%{_mandir}/man1/last.1*
%{_mandir}/man1/lastb.1*
%{_mandir}/man1/logger.1*
%{_mandir}/man1/login.1*
%{_mandir}/man1/look.1*
%{_mandir}/man1/lscpu.1*
%{_mandir}/man1/lsipc.1*
%{_mandir}/man1/lslogins.1*
%{_mandir}/man1/mcookie.1*
%{_mandir}/man1/mesg.1*
%{_mandir}/man1/more.1*
%{_mandir}/man1/mountpoint.1*
%{_mandir}/man1/namei.1*
#%{_mandir}/man1/nsenter.1*
%{_mandir}/man1/prlimit.1*
%{_mandir}/man1/rename.1*
%{_mandir}/man1/renice.1*
%{_mandir}/man1/rev.1*
%{_mandir}/man1/runuser.1*
%{_mandir}/man1/script.1*
%{_mandir}/man1/scriptreplay.1*
#%{_mandir}/man1/setpriv.1*
%{_mandir}/man1/setsid.1*
%{_mandir}/man1/setterm.1*
%{_mandir}/man1/su.1*
%{_mandir}/man1/tailf.1*
%{_mandir}/man1/taskset.1*
%{_mandir}/man1/ul.1*
%{_mandir}/man1/unshare.1*
%{_mandir}/man1/utmpdump.1.gz
%{_mandir}/man1/uuidgen.1*
%{_mandir}/man1/whereis.1*
%{_mandir}/man1/write.1*
%{_mandir}/man5/fstab.5*
%{_mandir}/man5/terminal-colors.d.5*
%{_mandir}/man8/addpart.8*
%{_mandir}/man8/agetty.8*
%{_mandir}/man8/blkdiscard.8*
%{_mandir}/man8/blkid.8*
%{_mandir}/man8/blockdev.8*
%{_mandir}/man8/chcpu.8*
%{_mandir}/man8/ctrlaltdel.8*
%{_mandir}/man8/delpart.8*
%{_mandir}/man8/fdisk.8*
%{_mandir}/man8/findfs.8*
%{_mandir}/man8/findmnt.8*
%{_mandir}/man8/fsck.8*
%{_mandir}/man8/fsck.cramfs.8*
%{_mandir}/man8/fsck.minix.8*
%{_mandir}/man8/fsfreeze.8*
%{_mandir}/man8/fstrim.8*
%{_mandir}/man8/isosize.8*
%{_mandir}/man8/ldattach.8*
%{_mandir}/man8/losetup.8*
%{_mandir}/man8/lsblk.8*
%{_mandir}/man8/lslocks.8.gz
%{_mandir}/man8/mkfs.8*
%{_mandir}/man8/mkfs.cramfs.8*
%{_mandir}/man8/mkfs.minix.8*
%{_mandir}/man8/mkswap.8*
%{_mandir}/man8/mount.8*
%{_mandir}/man8/nologin.8*
%{_mandir}/man8/partx.8*
%{_mandir}/man8/pivot_root.8*
%{_mandir}/man8/raw.8*
%{_mandir}/man8/rawdevices.8*
%{_mandir}/man8/readprofile.8*
%{_mandir}/man8/resizepart.8*
%{_mandir}/man8/rtcwake.8*
%{_mandir}/man8/setarch.8*
%{_mandir}/man8/sulogin.8.gz
%{_mandir}/man8/swaplabel.8*
%{_mandir}/man8/swapoff.8*
%{_mandir}/man8/swapon.8*
%{_mandir}/man8/switch_root.8*
%{_mandir}/man8/umount.8*
%{_mandir}/man8/uname26.8*
%{_mandir}/man8/wdctl.8.gz
%{_mandir}/man8/wipefs.8*
%{_mandir}/man8/zramctl.8*
%{_sbindir}/addpart
%{_sbindir}/agetty
%{_sbindir}/blkdiscard
%{_sbindir}/blkid
%{_sbindir}/blockdev
%{_sbindir}/chcpu
%{_sbindir}/ctrlaltdel
%{_sbindir}/delpart
%{_sbindir}/fdisk
%{_sbindir}/findfs
%{_sbindir}/fsck
%{_sbindir}/fsck.cramfs
%{_sbindir}/fsck.minix
%{_sbindir}/fsfreeze
%{_sbindir}/fstrim
%{_sbindir}/ldattach
%{_sbindir}/losetup
%{_sbindir}/mkfs
%{_sbindir}/mkfs.cramfs
%{_sbindir}/mkfs.minix
%{_sbindir}/mkswap
%{_sbindir}/nologin
%{_sbindir}/partx
%{_sbindir}/pivot_root
%{_sbindir}/readprofile
%{_sbindir}/resizepart
%{_sbindir}/rtcwake
%{_sbindir}/runuser
%{_sbindir}/sulogin
%{_sbindir}/swaplabel
%{_sbindir}/swapoff
%{_sbindir}/swapon
%{_sbindir}/switch_root
%{_sbindir}/wipefs
%{_sbindir}/zramctl
%{compldir}/addpart
%{compldir}/blkdiscard
%{compldir}/blkid
%{compldir}/blockdev
%{compldir}/cal
%{compldir}/chcpu
%{compldir}/chfn
%{compldir}/chrt
%{compldir}/chsh
%{compldir}/col
%{compldir}/colcrt
%{compldir}/colrm
%{compldir}/column
%{compldir}/ctrlaltdel
%{compldir}/delpart
%{compldir}/dmesg
%{compldir}/eject
%{compldir}/fallocate
%{compldir}/fdformat
%{compldir}/fdisk
%{compldir}/findmnt
%{compldir}/flock
%{compldir}/fsck
%{compldir}/fsck.cramfs
%{compldir}/fsck.minix
%{compldir}/fsfreeze
%{compldir}/fstrim
%{compldir}/getopt
%{compldir}/hexdump
%{compldir}/hwclock
%{compldir}/ionice
%{compldir}/ipcrm
%{compldir}/ipcs
%{compldir}/isosize
%{compldir}/last
%{compldir}/ldattach
%{compldir}/logger
%{compldir}/look
%{compldir}/losetup
%{compldir}/lsblk
%{compldir}/lscpu
%{compldir}/lsipc
%{compldir}/lslocks
%{compldir}/mcookie
%{compldir}/mesg
%{compldir}/mkfs
%{compldir}/mkfs.cramfs
%{compldir}/mkfs.minix
%{compldir}/mkswap
%{compldir}/more
%{compldir}/mountpoint
%{compldir}/namei
%{compldir}/partx
%{compldir}/pivot_root
%{compldir}/prlimit
%{compldir}/raw
%{compldir}/readprofile
%{compldir}/rename
%{compldir}/renice
%{compldir}/resizepart
%{compldir}/rev
%{compldir}/rtcwake
%{compldir}/runuser
%{compldir}/script
%{compldir}/scriptreplay
%{compldir}/setarch
%{compldir}/setsid
%{compldir}/setterm
%{compldir}/su
%{compldir}/swaplabel
%{compldir}/swapon
%{compldir}/tailf
%{compldir}/taskset
%{compldir}/ul
%{compldir}/unshare
%{compldir}/utmpdump
%{compldir}/uuidgen
%{compldir}/wdctl
%{compldir}/whereis
%{compldir}/wipefs
%{compldir}/write
%{compldir}/zramctl


%ifnarch s390 s390x
%{_sbindir}/clock
%{_sbindir}/fdformat
%{_sbindir}/hwclock
%{_mandir}/man8/fdformat.8*
%{_mandir}/man8/hwclock.8*
%{_mandir}/man8/clock.8*
%endif

%ifnarch %{sparc}
%{_sbindir}/cfdisk
%{_sbindir}/sfdisk
%{_mandir}/man8/cfdisk.8*
%{_mandir}/man8/sfdisk.8*
%{compldir}/cfdisk
%{compldir}/sfdisk
%endif

%ifarch %{sparc}
%{_bindir}/sunhostid
%endif

%ifarch %cytune_archs
%{_bindir}/cytune
%{_mandir}/man8/cytune.8*
%{compldir}/cytune
%endif


%files -n altiscale-uuidd
%defattr(-,root,root)
#%doc Documentation/licenses/COPYING.GPLv2
%{_mandir}/man8/uuidd.8*
%{_sbindir}/uuidd
#%{_unitdir}/uuidd.*
%dir %attr(2775, uuidd, uuidd) /var/lib/libuuid
%dir %attr(2775, uuidd, uuidd) /run/uuidd
%{compldir}/uuidd


%files -n altiscale-libmount
%defattr(-,root,root)
%doc libmount/COPYING
%{_libdir}/libmount.so.*

%files -n altiscale-libmount-devel
%defattr(-,root,root)
%doc libmount/COPYING
%{_libdir}/libmount.so
%{_includedir}/libmount
%{_libdir}/pkgconfig/mount.pc


%files -n altiscale-libblkid
%defattr(-,root,root)
%doc libblkid/COPYING
%{_libdir}/libblkid.so.*

%files -n altiscale-libblkid-devel
%defattr(-,root,root)
%doc libblkid/COPYING
%{_libdir}/libblkid.so
%{_includedir}/blkid
%{_mandir}/man3/libblkid.3*
%{_libdir}/pkgconfig/blkid.pc


%files -n altiscale-libuuid
%defattr(-,root,root)
%doc libuuid/COPYING
%{_libdir}/libuuid.so.*

%files -n altiscale-libuuid-devel
%defattr(-,root,root)
%doc libuuid/COPYING
%{_libdir}/libuuid.so
%{_includedir}/uuid
%{_mandir}/man3/uuid.3*
%{_mandir}/man3/uuid_clear.3*
%{_mandir}/man3/uuid_compare.3*
%{_mandir}/man3/uuid_copy.3*
%{_mandir}/man3/uuid_generate.3*
%{_mandir}/man3/uuid_generate_random.3*
%{_mandir}/man3/uuid_generate_time.3*
%{_mandir}/man3/uuid_generate_time_safe.3*
%{_mandir}/man3/uuid_is_null.3*
%{_mandir}/man3/uuid_parse.3*
%{_mandir}/man3/uuid_time.3*
%{_mandir}/man3/uuid_unparse.3*
%{_libdir}/pkgconfig/uuid.pc

%files -n altiscale-libfdisk
%defattr(-,root,root)
%{_libdir}/libfdisk.so.*

%files -n altiscale-libfdisk-devel
%defattr(-,root,root)
%{_libdir}/libfdisk.so
%{_includedir}/libfdisk
%{_libdir}/pkgconfig/fdisk.pc

%files -n altiscale-libsmartcols
%defattr(-,root,root)
%{_libdir}/libsmartcols.so.*

%files -n altiscale-libsmartcols-devel
%defattr(-,root,root)
%{_libdir}/libsmartcols.so
%{_includedir}/libsmartcols
%{_libdir}/pkgconfig/smartcols.pc

%changelog
