#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DNS
%define	pnam	ZoneParse
Summary:	DNS::ZoneParse - Parse and manipulate DNS Zone Files.
#Summary(pl):	
Name:		perl-DNS-ZoneParse
Version:	0.95
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	794fbdd533434bf06508bbb645fbc1e0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Storable >= 0.407
BuildRequires:	perl-Test-Simple >= 0.31
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will parse a Zone File and put all the Resource Records (RRs)
into an anonymous hash structure. At the moment, the following types of 
RRs are supported: SOA, NS, MX, A, CNAME, TXT, PTR. It could be useful for
maintaining DNS zones, or for transferring DNS zones to other servers. If
you want to generate an XML-friendly version of your zone files, it is
easy to use XML::Simple with this module once you have parsed the zonefile.

# %description -l pl
# TODO

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
