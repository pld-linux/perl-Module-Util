#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Util
%include	/usr/lib/rpm/macros.perl
Summary:	Module::Util - Module name tools and transformations
#Summary(pl.UTF-8):	
Name:		perl-Module-Util
Version:	1.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d9e5d48b7f1aee18582fab57f27cccfa
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Module-Util/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a few useful functions for manipulating module
names. Its main aim is to centralise some of the functions commonly
used by modules that manipulate other modules in some way, like
converting module names to relative paths.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Module/*.pm
%attr(755,root,root) %{_bindir}/pm_which
%{_mandir}/man1/pm_which.1p*
%{_mandir}/man3/*