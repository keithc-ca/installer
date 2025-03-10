%global upstream_version 11.0.25+9
# Only [A-Za-z0-9.] allowed in version:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/#_upstream_uses_invalid_characters_in_the_version
# also not very intuitive:
#  $ rpmdev-vercmp 11.0.13.0.1___7 11.0.13.0.0+8
#  11.0.13.0.0___8 == 11.0.13.0.0+8
%global spec_version 11.0.25.0.0.9
%global spec_release 1
%global priority 1111

%global source_url_base https://github.com/adoptium/temurin11-binaries/releases/download
%global upstream_version_url %(echo %{upstream_version} | sed 's/\+/%%2B/g')
%global upstream_version_no_plus %(echo %{upstream_version} | sed 's/\+/_/g')
%global java_provides openjdk

# Map architecture to the expected value in the download URL; Allow for a
# pre-defined value of vers_arch and use that if it's defined

%ifarch x86_64
%global vers_arch x64
%global vers_arch2 ppc64le
%global vers_arch3 s390x
%global vers_arch4 aarch64
%global vers_arch5 arm
%global src_num 0
%global sha_src_num 1
%endif
%ifarch ppc64le
%global vers_arch x64
%global vers_arch2 ppc64le
%global vers_arch3 s390x
%global vers_arch4 aarch64
%global vers_arch5 arm
%global src_num 2
%global sha_src_num 3
%endif
%ifarch s390x
%global vers_arch x64
%global vers_arch2 ppc64le
%global vers_arch3 s390x
%global vers_arch4 aarch64
%global vers_arch5 arm
%global src_num 4
%global sha_src_num 5
%endif
%ifarch aarch64
%global vers_arch x64
%global vers_arch2 ppc64le
%global vers_arch3 s390x
%global vers_arch4 aarch64
%global vers_arch5 arm
%global src_num 6
%global sha_src_num 7
%endif
%ifarch %{arm}
%global vers_arch x64
%global vers_arch2 ppc64le
%global vers_arch3 s390x
%global vers_arch4 aarch64
%global vers_arch5 arm
%global src_num 8
%global sha_src_num 9
%endif

# Allow for noarch SRPM build
%ifarch noarch
%global src_num 0
%global sha_src_num 1
%endif

Name:        temurin-11-jdk
Version:     %{spec_version}
Release:     %{spec_release}
Summary:     Eclipse Temurin 11 JDK

Group:       java
License:     GPLv2 with exceptions
Vendor:      Eclipse Adoptium
URL:         https://projects.eclipse.org/projects/adoptium
Packager:    Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org>

AutoReqProv: no
Prefix: %{_libdir}/jvm/%{name}

ExclusiveArch: x86_64 ppc64le s390x aarch64 %{arm}

BuildRequires:  tar
BuildRequires:  wget

Requires: /bin/sh
Requires: /usr/sbin/alternatives
Requires: ca-certificates
Requires: dejavu-fonts
Requires: libX11-6%{?_isa}
Requires: libXext6%{?_isa}
Requires: libXi6%{?_isa}
Requires: libXrender1%{?_isa}
Requires: libXtst6%{?_isa}
Requires: libasound2%{?_isa}
Requires: glibc%{?_isa}
Requires: libz1%{?_isa}
Requires: fontconfig%{?_isa}
Requires: libfreetype6%{?_isa}

Provides: java
Provides: java-11
Provides: java-11-devel
Provides: java-11-headless
Provides: java-11-%{java_provides}
Provides: java-11-%{java_provides}-devel
Provides: java-11-%{java_provides}-headless
Provides: java-devel
Provides: java-devel-%{java_provides}
Provides: java-headless
Provides: java-%{java_provides}
Provides: java-%{java_provides}-devel
Provides: java-%{java_provides}-headless
Provides: java-sdk
Provides: java-sdk-11
Provides: java-sdk-11-%{java_provides}
Provides: java-sdk-%{java_provides}
Provides: jre
Provides: jre-11
Provides: jre-11-headless
Provides: jre-11-%{java_provides}
Provides: jre-11-%{java_provides}-headless
Provides: jre-headless
Provides: jre-%{java_provides}
Provides: jre-%{java_provides}-headless

# First architecture (x86_64)
Source0: %{source_url_base}/jdk-%{upstream_version_url}/OpenJDK11U-jdk_%{vers_arch}_linux_hotspot_%{upstream_version_no_plus}.tar.gz
Source1: %{source_url_base}/jdk-%{upstream_version_url}/OpenJDK11U-jdk_%{vers_arch}_linux_hotspot_%{upstream_version_no_plus}.tar.gz.sha256.txt
# Second architecture (ppc64le)
Source2: %{source_url_base}/jdk-%{upstream_version_url}/OpenJDK11U-jdk_%{vers_arch2}_linux_hotspot_%{upstream_version_no_plus}.tar.gz
Source3: %{source_url_base}/jdk-%{upstream_version_url}/OpenJDK11U-jdk_%{vers_arch2}_linux_hotspot_%{upstream_version_no_plus}.tar.gz.sha256.txt
# Third architecture (s390x)
Source4: %{source_url_base}/jdk-%{upstream_version_url}/OpenJDK11U-jdk_%{vers_arch3}_linux_hotspot_%{upstream_version_no_plus}.tar.gz
Source5: %{source_url_base}/jdk-%{upstream_version_url}/OpenJDK11U-jdk_%{vers_arch3}_linux_hotspot_%{upstream_version_no_plus}.tar.gz.sha256.txt
# Fourth architecture (aarch64)
Source6: %{source_url_base}/jdk-%{upstream_version_url}/OpenJDK11U-jdk_%{vers_arch4}_linux_hotspot_%{upstream_version_no_plus}.tar.gz
Source7: %{source_url_base}/jdk-%{upstream_version_url}/OpenJDK11U-jdk_%{vers_arch4}_linux_hotspot_%{upstream_version_no_plus}.tar.gz.sha256.txt
# Fifth architecture (arm32)
Source8: %{source_url_base}/jdk-%{upstream_version_url}/OpenJDK11U-jdk_%{vers_arch5}_linux_hotspot_%{upstream_version_no_plus}.tar.gz
Source9: %{source_url_base}/jdk-%{upstream_version_url}/OpenJDK11U-jdk_%{vers_arch5}_linux_hotspot_%{upstream_version_no_plus}.tar.gz.sha256.txt

# Avoid build failures on some distros due to missing build-id in binaries.
%global debug_package %{nil}
%global __brp_strip %{nil}

%description
Eclipse Temurin JDK is an OpenJDK-based development environment to create
applications and components using the programming language Java.

%prep
pushd "%{_sourcedir}"
sha256sum -c "%{expand:%{SOURCE%{sha_src_num}}}"
popd

%setup -n jdk-%{upstream_version} -T -b %{src_num}

%build
# noop

%install
mkdir -p %{buildroot}%{prefix}
cd %{buildroot}%{prefix}
tar --strip-components=1 -C "%{buildroot}%{prefix}" -xf %{expand:%{SOURCE%{src_num}}}

# Strip bundled Freetype and use OS package instead.
rm -f "%{buildroot}%{prefix}/lib/libfreetype.so"

# Use cacerts included in OS
rm -f "%{buildroot}%{prefix}/lib/security/cacerts"
pushd "%{buildroot}%{prefix}/lib/security"
ln -s /var/lib/ca-certificates/java-cacerts "%{buildroot}%{prefix}/lib/security/cacerts"
popd

%pretrans
# noop

%post
if [ $1 -ge 1 ] ; then
    update-alternatives --install %{_bindir}/java java %{prefix}/bin/java %{priority} \
                        --slave %{_bindir}/jjs jjs %{prefix}/bin/jjs \
                        --slave %{_bindir}/keytool keytool %{prefix}/bin/keytool \
                        --slave %{_bindir}/pack200 pack200 %{prefix}/bin/pack200 \
                        --slave %{_bindir}/rmid rmid %{prefix}/bin/rmid \
                        --slave %{_bindir}/rmiregistry rmiregistry %{prefix}/bin/rmiregistry \
                        --slave %{_bindir}/unpack200 unpack200 %{prefix}/bin/unpack200 \
                        --slave %{_bindir}/jexec jexec %{prefix}/lib/jexec \
                        --slave %{_bindir}/jspawnhelper jspawnhelper %{prefix}/lib/jspawnhelper \
                        --slave  %{_mandir}/man1/java.1 java.1 %{prefix}/man/man1/java.1 \
                        --slave  %{_mandir}/man1/jjs.1 jjs.1 %{prefix}/man/man1/jjs.1 \
                        --slave  %{_mandir}/man1/keytool.1 keytool.1 %{prefix}/man/man1/keytool.1 \
                        --slave  %{_mandir}/man1/pack200.1 pack200.1 %{prefix}/man/man1/pack200.1 \
                        --slave  %{_mandir}/man1/rmid.1 rmid.1 %{prefix}/man/man1/rmid.1 \
                        --slave  %{_mandir}/man1/rmiregistry.1 rmiregistry.1 %{prefix}/man/man1/rmiregistry.1 \
                        --slave  %{_mandir}/man1/unpack200.1 unpack200.1 %{prefix}/man/man1/unpack200.1

    update-alternatives --install %{_bindir}/javac javac %{prefix}/bin/javac %{priority} \
                        --slave %{_bindir}/jaotc jaotc %{prefix}/bin/jaotc \
                        --slave %{_bindir}/jar jar %{prefix}/bin/jar \
                        --slave %{_bindir}/jarsigner jarsigner %{prefix}/bin/jarsigner \
                        --slave %{_bindir}/javadoc javadoc %{prefix}/bin/javadoc \
                        --slave %{_bindir}/javap javap %{prefix}/bin/javap \
                        --slave %{_bindir}/jcmd jcmd %{prefix}/bin/jcmd \
                        --slave %{_bindir}/jconsole jconsole %{prefix}/bin/jconsole \
                        --slave %{_bindir}/jdb jdb %{prefix}/bin/jdb \
                        --slave %{_bindir}/jdeprscan jdeprscan %{prefix}/bin/jdeprscan \
                        --slave %{_bindir}/jdeps jdeps %{prefix}/bin/jdeps \
                        --slave %{_bindir}/jfr jfr %{prefix}/bin/jfr \
                        --slave %{_bindir}/jhsdb jhsdb %{prefix}/bin/jhsdb \
                        --slave %{_bindir}/jimage jimage %{prefix}/bin/jimage \
                        --slave %{_bindir}/jinfo jinfo %{prefix}/bin/jinfo \
                        --slave %{_bindir}/jlink jlink %{prefix}/bin/jlink \
                        --slave %{_bindir}/jmap jmap %{prefix}/bin/jmap \
                        --slave %{_bindir}/jmod jmod %{prefix}/bin/jmod \
                        --slave %{_bindir}/jps jps %{prefix}/bin/jps \
                        --slave %{_bindir}/jrunscript jrunscript %{prefix}/bin/jrunscript \
                        --slave %{_bindir}/jshell jshell %{prefix}/bin/jshell \
                        --slave %{_bindir}/jstack jstack %{prefix}/bin/jstack \
                        --slave %{_bindir}/jstat jstat %{prefix}/bin/jstat \
                        --slave %{_bindir}/jstatd jstatd %{prefix}/bin/jstatd \
                        --slave %{_bindir}/rmic rmic %{prefix}/bin/rmic \
                        --slave %{_bindir}/serialver serialver %{prefix}/bin/serialver \
                        --slave  %{_mandir}/man1/jar.1 jar.1 %{prefix}/man/man1/jar.1 \
                        --slave  %{_mandir}/man1/jarsigner.1 jarsigner.1 %{prefix}/man/man1/jarsigner.1 \
                        --slave  %{_mandir}/man1/javac.1 javac.1 %{prefix}/man/man1/javac.1 \
                        --slave  %{_mandir}/man1/javadoc.1 javadoc.1 %{prefix}/man/man1/javadoc.1 \
                        --slave  %{_mandir}/man1/javap.1 javap.1 %{prefix}/man/man1/javap.1 \
                        --slave  %{_mandir}/man1/jcmd.1 jcmd.1 %{prefix}/man/man1/jcmd.1 \
                        --slave  %{_mandir}/man1/jconsole.1 jconsole.1 %{prefix}/man/man1/jconsole.1 \
                        --slave  %{_mandir}/man1/jdb.1 jdb.1 %{prefix}/man/man1/jdb.1 \
                        --slave  %{_mandir}/man1/jdeps.1 jdeps.1 %{prefix}/man/man1/jdeps.1 \
                        --slave  %{_mandir}/man1/jinfo.1 jinfo.1 %{prefix}/man/man1/jinfo.1 \
                        --slave  %{_mandir}/man1/jmap.1 jmap.1 %{prefix}/man/man1/jmap.1 \
                        --slave  %{_mandir}/man1/jps.1 jps.1 %{prefix}/man/man1/jps.1 \
                        --slave  %{_mandir}/man1/jrunscript.1 jrunscript.1 %{prefix}/man/man1/jrunscript.1 \
                        --slave  %{_mandir}/man1/jstack.1 jstack.1 %{prefix}/man/man1/jstack.1 \
                        --slave  %{_mandir}/man1/jstat.1 jstat.1 %{prefix}/man/man1/jstat.1 \
                        --slave  %{_mandir}/man1/jstatd.1 jstatd.1 %{prefix}/man/man1/jstatd.1 \
                        --slave  %{_mandir}/man1/rmic.1 rmic.1 %{prefix}/man/man1/rmic.1 \
                        --slave  %{_mandir}/man1/serialver.1 serialver.1 %{prefix}/man/man1/serialver.1
fi

%preun
if [ $1 -eq 0 ]; then
    update-alternatives --remove java %{prefix}/bin/java
    update-alternatives --remove javac %{prefix}/bin/javac
fi

%files
%defattr(-,root,root)
%{prefix}

%changelog
* Wed Oct 16 2024 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.25.0.0.9-1
- Eclipse Temurin 11.0.25.0+9 release.
* Wed Jul 17 2024 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.24.0.0.8-1
- Eclipse Temurin 11.0.24.0+8 release.
* Wed Apr 17 2024 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.23.0.0.9-1
- Eclipse Temurin 11.0.23.0+9 release.
* Mon Jan 23 2024 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.22.0.0.7-1
- Eclipse Temurin 11.0.22.0+7 release.
* Thu Oct 26 2023 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.21.0.0.1-9
- Eclipse Temurin 11.0.21.0+9 release.
* Thu Aug 31 2023 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.20.1.0.1-1
- Eclipse Temurin 11.0.20.1+1 release.
* Tue Jul 25 2023 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.20.0.0.8-1
- Eclipse Temurin 11.0.20+8 release.
* Thu May 4 2023 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.19.0.0.7-2
- Fix alternatives linking.
* Wed Apr 26 2023 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.19.0.0.7-1
- Eclipse Temurin 11.0.19+7 release.
* Wed Feb 22 2023 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.18.0.0.10-2
- Eclipse Temurin 11.0.18+10 release 2.
* Wed Jan 18 2023 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.18.0.0.10-1
- Eclipse Temurin 11.0.18+10 release.
* Thu Oct 27 2022 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.17.0.0.8-1
- Eclipse Temurin 11.0.17+8 release.
* Tue Aug 23 2022 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.16.1.0.1-1
- Eclipse Temurin 11.0.16.1+1 release.
* Tue Jul 26 2022 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.16.0.0.8-1
- Eclipse Temurin 11.0.16.0+8 release.
* Wed Apr 27 2022 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.15.0.0.10-1
- Eclipse Temurin 11.0.15.0+10 release.
* Thu Feb 10 2022 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.14.1.0.1-1
- Eclipse Temurin 11.0.14.1+1 release.
* Tue Feb 1 2022 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.14.0.0.9-1
- Eclipse Temurin 11.0.14+9 release.
* Tue Aug 10 2021 Eclipse Adoptium Package Maintainers <temurin-dev@eclipse.org> 11.0.12.0.0.7-1
- Eclipse Temurin 11.0.12+7 release.
