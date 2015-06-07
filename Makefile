BASE_DIR = $(shell pwd)
DOC_SRCDIR=$(BASE_DIR)/src
DOC_BUILDDIR=$(BASE_DIR)/build
SPHINXOPTS = -n -c $(DOC_SRCDIR) \
			 -A local=1 \
			 $(DOC_SRCDIR)
SPHINX_BUILD=$(BASE_DIR)/sphinx-build

all: html pdf texinfo

html:
	@mkdir -p $(DOC_BUILDDIR)
	$(SPHINX_BUILD) -b html $(SPHINXOPTS) $(DOC_BUILDDIR)/html

pdf:
	@mkdir -p $(DOC_BUILDDIR)
	$(SPHINX_BUILD) -b latex $(SPHINXOPTS) $(DOC_BUILDDIR)/latex
	$(MAKE) -C $(DOC_BUILDDIR)/latex all-pdf

texinfo:
	@mkdir -p $(DOC_BUILDDIR)
	$(SPHINX_BUILD) -b texinfo $(SPHINXOPTS) $(DOC_BUILDDIR)/texinfo
	$(MAKE) -C $(DOC_BUILDDIR)/texinfo info

clean:
	rm -rf $(DOC_BUILDDIR)/textinfo
	rm -rf $(DOC_BUILDDIR)/latex
	rm -rf $(DOC_BUILDDIR)/html
	rm -rf $(DOC_BUILDDIR)/doctrees

