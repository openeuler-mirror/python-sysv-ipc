%global _empty_manifest_terminate_build 0
Name:           python-sysv-ipc
Version:        1.1.0
Release:        1
Summary:        System V IPC primitives (semaphores, shared memory and message queues) for Python
License:        BSD
URL:            http://semanchuk.com/philip/sysv_ipc/
Source0:        https://files.pythonhosted.org/packages/0c/d7/5d2f861155e9749f981e6c58f2a482d3ab458bf8c35ae24d4b4d5899ebf9/sysv_ipc-1.1.0.tar.gz
%description
System V IPC primitives (semaphores, shared memory and message queues) for Python

%package -n python3-sysv-ipc
Summary:        System V IPC primitives (semaphores, shared memory and message queues) for Python
Provides:       python-sysv-ipc
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi
BuildRequires:  gcc
BuildRequires:  gdb
%description -n python3-sysv-ipc
System V IPC primitives (semaphores, shared memory and message queues) for Python

%package help
Summary:        System V IPC primitives (semaphores, shared memory and message queues) for Python
Provides:       python3-sysv-ipc-doc
%description help
System V IPC primitives (semaphores, shared memory and message queues) for Python

%prep
%autosetup -n sysv_ipc-%{version}

%build
%py3_build

%install
%py3_install

install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
%{__python3} setup.py test

%files -n python3-sysv-ipc -f filelist.lst

%dir %{python3_sitearch}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue Aug 03 2021 OpenStack_SIG <openstack@openeuler.org> - 1.1.0-1
- Package Spec generate
