#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-daemon
Version  : 1.0.13
Release  : 1
URL      : https://repo1.maven.org/maven2/commons-daemon/commons-daemon/1.0.13/commons-daemon-1.0.13.jar
Source0  : https://repo1.maven.org/maven2/commons-daemon/commons-daemon/1.0.13/commons-daemon-1.0.13.jar
Source1  : https://repo1.maven.org/maven2/commons-daemon/commons-daemon/1.0.13/commons-daemon-1.0.13.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-daemon-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-daemon package.
Group: Data

%description data
data components for the mvn-commons-daemon package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-daemon/commons-daemon/1.0.13
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/commons-daemon/commons-daemon/1.0.13

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-daemon/commons-daemon/1.0.13
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/commons-daemon/commons-daemon/1.0.13


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/commons-daemon/commons-daemon/1.0.13/commons-daemon-1.0.13.jar
/usr/share/java/.m2/repository/commons-daemon/commons-daemon/1.0.13/commons-daemon-1.0.13.pom