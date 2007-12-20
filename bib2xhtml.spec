%define name	bib2xhtml
%define version	2.26
%define release	%mkrel 2

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

