#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DNS
%define	pnam	ZoneParse
Summary:	DNS::ZoneParse - parse and manipulate DNS zone files
Summary(pl.UTF-8):	DNS::ZoneParse - analiza i obróbka plików stref DNS
Name:		perl-DNS-ZoneParse
Version:	0.96
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7709985332ced4080fb4100c03ebeccd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Storable >= 0.407
BuildRequires:	perl-Test-Simple >= 0.31
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will parse a Zone File and put all the Resource Records
(RRs) into an anonymous hash structure. At the moment, the following
types of RRs are supported: SOA, NS, MX, A, CNAME, TXT, PTR. It could
be useful for maintaining DNS zones, or for transferring DNS zones to
other servers. If you want to generate an XML-friendly version of your
zone files, it is easy to use XML::Simple with this module once you
have parsed the zonefile.

%description -l pl.UTF-8
Ten moduł przetwarza pliki stref i umieszcza wszystkie rekordy zasobów
(Resource Records, w skrócie RR) w anonimowej strukturze będącej
tablicą asocjacyjną. Aktualnie obsługiwane są następujące rodzaje
rekordów: SOA, NS, MX, A, CNAME, TXT, PTR. Może to być przydatne przy
zarządzaniu strefami DNS albo przekazywaniu stref na inne serwery.
Jeśli chcemy wygenerować przyjazną dla XML wersję plików stref, można
łatwo użyć XML::Simple wraz z tym modułem zaraz po przeanalizowaniu
pliku strefy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/DNS/*.pm
%{_mandir}/man3/*
