#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/BINDINGS/python/python-emotion python-emotion; \
#cd python-emotion; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf python-emotion-$PKG_VERSION.tar.xz python-emotion/ --exclude .svn --exclude .*ignore

Summary:	Ethumb bindings for Python
Name:		python-ethumb
Version:	1.7.0
Release:	1
Group:		Graphical desktop/Enlightenment
License:	GPLv2
URL:		https://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(ethumb)
BuildRequires:	pkgconfig(ethumb_client)
BuildRequires:	python-cython
BuildRequires:  python-devel

%description
Python support files for Ethumb.

%package devel
Summary:	Development files for %{name}
Group:		Development/Python

%description devel
Development files for the Python wrapper for the Ethumb libraries.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README
%{py_platsitedir}/ethumb/*

%files devel
%{_datadir}/%{name}/*
%{_libdir}/pkgconfig/*.pc

