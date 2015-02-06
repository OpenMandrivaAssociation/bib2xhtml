%define name	bib2xhtml
%define version	2.35
%define release	3

%define bstdir /usr/share/texmf/bibtex/bst/bib2xhtml

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A program for converting BibTeX files into XHTML 1.0
License:	GPL 
Group:		Publishing
Url:		http://www.spinellis.gr/sw/textproc/bib2xhtml/
Source:		http://www.spinellis.gr/sw/textproc/bib2xhtml/%{name}-%{version}.tar.bz2
Requires:	tetex
Requires:	perl(PDF::API2)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
bib2xhtml is a program that converts BibTeX files into HTML
(specifically XHTML 1.0). The conversion is mostly done by specialized
BibTeX style files derived from converted bibliography style
templates. This ensures that the original BibTeX styles are faithfully
reproduced. Some postprocessing is performed by Perl code.

%prep
%setup -q
# fix encoding
perl -pi -e 'tr/\r//d' *.html *.bib bib2xhtml

%build

%install
rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{_bindir} 
install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 755 -d %{buildroot}%{bstdir}
install -m 755 bib2xhtml %{buildroot}%{_bindir}
install -m 644 bib2xhtml.man %{buildroot}%{_mandir}/man1/bib2xhtml.1
install -m 644 *.bst %{buildroot}%{bstdir}

%post
texhash

%postun
rm -rf %bstdir
texhash

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README *.html *.txt *.pdf example.bib
%{_bindir}/bib2xhtml
%{_mandir}/man1/bib2xhtml.1.*
%{bstdir}/*



%changelog
* Mon Dec 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.35-2mdv2011.0
+ Revision: 623434
- update to new version 2.35

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.31-2mdv2011.0
+ Revision: 610065
- rebuild

* Mon Feb 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.31-1mdv2010.1
+ Revision: 502469
- update to new version 2.31

* Thu Jul 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.30-1mdv2010.0
+ Revision: 396683
- update to new version 2.30

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.26-4mdv2009.0
+ Revision: 243235
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 2.26-2mdv2008.1
+ Revision: 135829
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.26-2mdv2008.0
+ Revision: 64662
- fix perl dependency (close #32293)

* Thu Jun 14 2007 Lev Givon <lev@mandriva.org> 2.26-1mdv2008.0
+ Revision: 39787
- Update to 2.26.


* Tue Jun 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.23-1mdv2007.0
- New release 2.23

* Tue Sep 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.20-1mdk
- contributed by  Lev Givon (<lev@columbia.edu>)

