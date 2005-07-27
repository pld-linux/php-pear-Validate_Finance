%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	Finance
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Validation class for finance
Summary(pl):	%{_pearname} - Klasa sprawdzaj±ca poprawno¶æ dla finansów
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	bbf5ccee532c874d32603b1e10f21d1b
URL:		http://pear.php.net/package/Validate_Finance/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear >= 4:1.0-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package to validate Finance data. It includes:
- IBAN

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet do sprawdzania poprawno¶ci danych finansowych. Dotyczy to:
- numerów IBAN

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
