%global bstdir /usr/share/texmf/bibtex/bst/bib2xhtml

Summary:	A program for converting BibTeX files into XHTML 1.0
Name:		bib2xhtml
Version:	3.0
Release:	1
License:	GPL 
Group:		Publishing
Url:		https://www.spinellis.gr/sw/textproc/bib2xhtml/
#Source0:	https://www.spinellis.gr/sw/textproc/bib2xhtml/%{name}-v%{version}.tar.gz
Source0:	https://github.com/dspinellis/bib2xhtml/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:	texlive-tetex
Requires:	perl(PDF::API2)

BuildArch:	noarch

%description
bib2xhtml is a program that converts BibTeX files into HTML
(specifically XHTML 1.0). The conversion is mostly done by specialized
BibTeX style files derived from converted bibliography style
templates. This ensures that the original BibTeX styles are faithfully
reproduced. Some postprocessing is performed by Perl code.

%files
%license COPYING
%doc ChangeLog *.html *.pdf example.bib
%{_bindir}/bib2xhtml
%{_mandir}/man1/bib2xhtml.1.*
%{bstdir}/*

#--------------------------------------------------------------------

%prep
%autosetup -p1

# fix encoding
perl -pi -e 'tr/\r//d' *.html *.bib bib2xhtml

%build
perl gen-bst

%install
install -pm 0755 -d %{buildroot}%{_bindir} 
install -pm 0755 -d %{buildroot}%{_mandir}/man1
install -pm 0755 -d %{buildroot}%{bstdir}
install -pm 0755 bib2xhtml %{buildroot}%{_bindir}
install -pm 0644 bib2xhtml.man %{buildroot}%{_mandir}/man1/bib2xhtml.1
install -pm 0644 *.bst %{buildroot}%{bstdir}

%post
texhash

%postun
rm -rf %bstdir
texhash

