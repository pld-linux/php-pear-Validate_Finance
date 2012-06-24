%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	Finance
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Validation class for finance
Summary(pl):	%{_pearname} - Klasa sprawdzaj�ca poprawno�� dla finans�w
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	1.1
Epoch:		0
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	bbf5ccee532c874d32603b1e10f21d1b
URL:		http://pear.php.net/package/Validate_Finance/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear >= 4:1.0-4
Requires:	php-common >= 3:4.2.0
Requires:	php-pear-Validate >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package to validate Finance data. It includes:
- IBAN

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet do sprawdzania poprawno�ci danych finansowych. Dotyczy to:
- numer�w IBAN

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
