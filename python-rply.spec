%global pypi_name rply

Name:           python-%{pypi_name}
Version:        0.7.8
Release:        3
Summary:        An attempt to port David Beazley's PLY to RPython, and give it a cooler API.
License:        BSD 3-Clause
URL:            https://github.com/alex/rply
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

Provides:	python-%{pypi_name} = %{EVRD}

%description
A pure Python parser generator, that also works with RPython. 
It is a more-or-less direct port of David Beazley's awesome PLY, with a new public API, and RPython support.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -vrf *.egg-info

%build
%py_build

%install
%py_install

%files -n python-%{pypi_name}
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-*.egg-info/
