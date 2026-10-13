%global pypi_name rply

Name:           python-%{pypi_name}
Version:        0.7.8
Release:        6
Summary:        Parser generator based on PLY, with an RPython-friendly API
Group:          Development/Python
License:        BSD-3-Clause
URL:            https://github.com/alex/rply
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(setuptools)

Provides:	python-%{pypi_name} = %{EVRD}

%description
A pure Python parser generator that also works with RPython.
It is a port of David Beazley's PLY, with a new public API and
RPython support.

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
