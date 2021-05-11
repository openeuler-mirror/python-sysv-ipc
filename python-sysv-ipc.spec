%global _empty_manifest_terminate_build 0
Name:		python-sysv-ipc
Version:	1.0.0
Release:	1
Summary:	System V IPC primitives (semaphores, shared memory and message queues) for Python
License:	BSD
URL:		http://semanchuk.com/philip/sysv_ipc/
Source0:	https://files.pythonhosted.org/packages/08/7d/a862f3045fa191eeece23650725273f2ccaf9ac6b95443dfe4cac6508638/sysv_ipc-1.0.0.tar.gz
%description


%package -n python2-sysv-ipc
Summary:	System V IPC primitives (semaphores, shared memory and message queues) for Python
Provides:	python2-sysv-ipc
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
%description -n python2-sysv-ipc


%package help
Summary:	Development documents and examples for sysv-ipc
Provides:	python2-sysv-ipc-doc
%description help


%prep
%autosetup -n sysv_ipc-1.0.0

%build
%py2_build

%install
%py2_install
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

%files -n python2-sysv-ipc -f filelist.lst
%dir %{python2_sitearch}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue May 11 2021 OpenStack_SIG <openstack@openeuler.org>
- Package Spec generated
