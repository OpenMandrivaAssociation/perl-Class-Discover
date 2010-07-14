%define upstream_name    Class-Discover
%define upstream_version 1.000003

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Detect MooseX::Declare's 'class' keyword in files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MM_Unix)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::Find::Rule::Perl)
BuildRequires: perl(File::Temp)
BuildRequires: perl(PPI)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This class is designed primarily for tools that whish to populate the
'provides' field of META.{yml,json} files so that the CPAN indexer will pay
attention to the existance of your classes, rather than blithely ignoring
them.

The version parsing is basically the same as what M::I's '->version_form'
does, so should hopefully work as well as it does.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


