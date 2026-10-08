Name:           oobackup
Version:        0.2.0
Release:        1%{?dist}
Summary:        Content-addressed snapshot utility creating deduplicated incremental trees.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oobackup
Source0:        oobackup-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oobackup is a sovereign, capability-bounded SNAPSHOT ENGINE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oobackup
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oobackup-uninstall

%files
/usr/bin/oobackup
/usr/bin/oobackup-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign snapshot engine and deduplicated content-addressed repository
