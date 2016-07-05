#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : file
Version  : 5.26
Release  : 22
URL      : ftp://ftp.astron.com/pub/file/file-5.26.tar.gz
Source0  : ftp://ftp.astron.com/pub/file/file-5.26.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: file-bin
Requires: file-lib
Requires: file-data
Requires: file-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : python-dev
BuildRequires : setuptools
BuildRequires : zlib-dev
Patch1: stateless.patch

%description
Mailing List: file@mx.gw.com
Mailing List archives: http://mx.gw.com/pipermail/file/
Bug tracker: http://bugs.gw.com/
E-mail: christos@astron.com

%package bin
Summary: bin components for the file package.
Group: Binaries
Requires: file-data

%description bin
bin components for the file package.


%package data
Summary: data components for the file package.
Group: Data

%description data
data components for the file package.


%package dev
Summary: dev components for the file package.
Group: Development
Requires: file-lib
Requires: file-bin
Requires: file-data
Provides: file-devel

%description dev
dev components for the file package.


%package doc
Summary: doc components for the file package.
Group: Documentation

%description doc
doc components for the file package.


%package lib
Summary: lib components for the file package.
Group: Libraries
Requires: file-data

%description lib
lib components for the file package.


%prep
%setup -q -n file-5.26
%patch1 -p1

%build
export LANG=C
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/file

%files data
%defattr(-,root,root,-)
/usr/share/file/magic.mgc

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man4/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
