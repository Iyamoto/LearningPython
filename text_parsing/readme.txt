>>> help(item)
Help on HtmlElement in module lxml.html object:

class HtmlElement(lxml.etree.ElementBase, HtmlMixin)
 |  Method resolution order:
 |      HtmlElement
 |      lxml.etree.ElementBase
 |      lxml.etree._Element
 |      HtmlMixin
 |      builtins.object
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from lxml.etree.ElementBase:
 |  
 |  __init__(...)
 |      ElementBase(*children, attrib=None, nsmap=None, **_extra)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from lxml.etree.ElementBase:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from lxml.etree._Element:
 |  
 |  __bool__(...)
 |      x.__bool__() <==> x != 0
 |  
 |  __contains__(...)
 |      __contains__(self, element)
 |  
 |  __copy__(...)
 |      __copy__(self)
 |  
 |  __deepcopy__(...)
 |      __deepcopy__(self, memo)
 |  
 |  __delitem__(...)
 |      __delitem__(self, x)
 |      
 |      Deletes the given subelement or a slice.
 |  
 |  __getitem__(...)
 |      Returns the subelement at the given position or the requested
 |      slice.
 |  
 |  __iter__(...)
 |      __iter__(self)
 |  
 |  __len__(...)
 |      __len__(self)
 |      
 |      Returns the number of subelements.
 |  
 |  __repr__(...)
 |      __repr__(self)
 |  
 |  __reversed__(...)
 |      __reversed__(self)
 |  
 |  __setitem__(...)
 |      __setitem__(self, x, value)
 |      
 |      Replaces the given subelement index or slice.
 |  
 |  addnext(...)
 |      addnext(self, element)
 |      
 |      Adds the element as a following sibling directly after this
 |      element.
 |      
 |      This is normally used to set a processing instruction or comment after
 |      the root node of a document.  Note that tail text is automatically
 |      discarded when adding at the root level.
 |  
 |  addprevious(...)
 |      addprevious(self, element)
 |      
 |      Adds the element as a preceding sibling directly before this
 |      element.
 |      
 |      This is normally used to set a processing instruction or comment
 |      before the root node of a document.  Note that tail text is
 |      automatically discarded when adding at the root level.
 |  
 |  append(...)
 |      append(self, element)
 |      
 |      Adds a subelement to the end of this element.
 |  
 |  clear(...)
 |      clear(self)
 |      
 |      Resets an element.  This function removes all subelements, clears
 |      all attributes and sets the text and tail properties to None.
 |  
 |  extend(...)
 |      extend(self, elements)
 |      
 |      Extends the current children by the elements in the iterable.
 |  
 |  find(...)
 |      find(self, path, namespaces=None)
 |      
 |      Finds the first matching subelement, by tag name or path.
 |      
 |      The optional ``namespaces`` argument accepts a
 |      prefix-to-namespace mapping that allows the usage of XPath
 |      prefixes in the path expression.
 |  
 |  findall(...)
 |      findall(self, path, namespaces=None)
 |      
 |      Finds all matching subelements, by tag name or path.
 |      
 |      The optional ``namespaces`` argument accepts a
 |      prefix-to-namespace mapping that allows the usage of XPath
 |      prefixes in the path expression.
 |  
 |  findtext(...)
 |      findtext(self, path, default=None, namespaces=None)
 |      
 |      Finds text for the first matching subelement, by tag name or path.
 |      
 |      The optional ``namespaces`` argument accepts a
 |      prefix-to-namespace mapping that allows the usage of XPath
 |      prefixes in the path expression.
 |  
 |  get(...)
 |      get(self, key, default=None)
 |      
 |      Gets an element attribute.
 |  
 |  getchildren(...)
 |      getchildren(self)
 |      
 |      Returns all direct children.  The elements are returned in document
 |      order.
 |      
 |      :deprecated: Note that this method has been deprecated as of
 |        ElementTree 1.3 and lxml 2.0.  New code should use
 |        ``list(element)`` or simply iterate over elements.
 |  
 |  getiterator(...)
 |      getiterator(self, tag=None, *tags)
 |      
 |      Returns a sequence or iterator of all elements in the subtree in
 |      document order (depth first pre-order), starting with this
 |      element.
 |      
 |      Can be restricted to find only elements with a specific tag,
 |      see `iter`.
 |      
 |      :deprecated: Note that this method is deprecated as of
 |        ElementTree 1.3 and lxml 2.0.  It returns an iterator in
 |        lxml, which diverges from the original ElementTree
 |        behaviour.  If you want an efficient iterator, use the
 |        ``element.iter()`` method instead.  You should only use this
 |        method in new code if you require backwards compatibility
 |        with older versions of lxml or ElementTree.
 |  
 |  getnext(...)
 |      getnext(self)
 |      
 |      Returns the following sibling of this element or None.
 |  
 |  getparent(...)
 |      getparent(self)
 |      
 |      Returns the parent of this element or None for the root element.
 |  
 |  getprevious(...)
 |      getprevious(self)
 |      
 |      Returns the preceding sibling of this element or None.
 |  
 |  getroottree(...)
 |      getroottree(self)
 |      
 |      Return an ElementTree for the root node of the document that
 |      contains this element.
 |      
 |      This is the same as following element.getparent() up the tree until it
 |      returns None (for the root element) and then build an ElementTree for
 |      the last parent that was returned.
 |  
 |  index(...)
 |      index(self, child, start=None, stop=None)
 |      
 |      Find the position of the child within the parent.
 |      
 |      This method is not part of the original ElementTree API.
 |  
 |  insert(...)
 |      insert(self, index, element)
 |      
 |      Inserts a subelement at the given position in this element
 |  
 |  items(...)
 |      items(self)
 |      
 |      Gets element attributes, as a sequence. The attributes are returned in
 |      an arbitrary order.
 |  
 |  iter(...)
 |      iter(self, tag=None, *tags)
 |      
 |      Iterate over all elements in the subtree in document order (depth
 |      first pre-order), starting with this element.
 |      
 |      Can be restricted to find only elements with a specific tag:
 |      pass ``"{ns}localname"`` as tag. Either or both of ``ns`` and
 |      ``localname`` can be ``*`` for a wildcard; ``ns`` can be empty
 |      for no namespace. ``"localname"`` is equivalent to ``"{}localname"``
 |      (i.e. no namespace) but ``"*"`` is ``"{*}*"`` (any or no namespace),
 |      not ``"{}*"``.
 |      
 |      You can also pass the Element, Comment, ProcessingInstruction and
 |      Entity factory functions to look only for the specific element type.
 |      
 |      Passing more than one tag will let the iterator return all elements
 |      matching any of these tags, in document order.
 |  
 |  iterancestors(...)
 |      iterancestors(self, tag=None, *tags)
 |      
 |      Iterate over the ancestors of this element (from parent to parent).
 |      
 |      Can be restricted to find only elements with a specific tag,
 |      see `iter`.
 |  
 |  iterchildren(...)
 |      iterchildren(self, tag=None, *tags, reversed=False)
 |      
 |      Iterate over the children of this element.
 |      
 |      As opposed to using normal iteration on this element, the returned
 |      elements can be reversed with the 'reversed' keyword and restricted
 |      to find only elements with a specific tag, see `iter`.
 |  
 |  iterdescendants(...)
 |      iterdescendants(self, tag=None, *tags)
 |      
 |      Iterate over the descendants of this element in document order.
 |      
 |      As opposed to ``el.iter()``, this iterator does not yield the element
 |      itself.  The returned elements can be restricted to find only elements
 |      with a specific tag, see `iter`.
 |  
 |  iterfind(...)
 |      iterfind(self, path, namespaces=None)
 |      
 |      Iterates over all matching subelements, by tag name or path.
 |      
 |      The optional ``namespaces`` argument accepts a
 |      prefix-to-namespace mapping that allows the usage of XPath
 |      prefixes in the path expression.
 |  
 |  itersiblings(...)
 |      itersiblings(self, tag=None, *tags, preceding=False)
 |      
 |      Iterate over the following or preceding siblings of this element.
 |      
 |      The direction is determined by the 'preceding' keyword which
 |      defaults to False, i.e. forward iteration over the following
 |      siblings.  When True, the iterator yields the preceding
 |      siblings in reverse document order, i.e. starting right before
 |      the current element and going backwards.
 |      
 |      Can be restricted to find only elements with a specific tag,
 |      see `iter`.
 |  
 |  itertext(...)
 |      itertext(self, tag=None, *tags, with_tail=True)
 |      
 |      Iterates over the text content of a subtree.
 |      
 |      You can pass a tag name to restrict text content to specific elements,
 |      see `iter`.
 |      
 |      You can set the ``with_tail`` keyword argument to ``False`` to skip
 |      over tail text.
 |  
 |  keys(...)
 |      keys(self)
 |      
 |      Gets a list of attribute names.  The names are returned in an
 |      arbitrary order (just like for an ordinary Python dictionary).
 |  
 |  makeelement(...)
 |      makeelement(self, _tag, attrib=None, nsmap=None, **_extra)
 |      
 |      Creates a new element associated with the same document.
 |  
 |  remove(...)
 |      remove(self, element)
 |      
 |      Removes a matching subelement. Unlike the find methods, this
 |      method compares elements based on identity, not on tag value
 |      or contents.
 |  
 |  replace(...)
 |      replace(self, old_element, new_element)
 |      
 |      Replaces a subelement with the element passed as second argument.
 |  
 |  set(...)
 |      set(self, key, value)
 |      
 |      Sets an element attribute.
 |  
 |  values(...)
 |      values(self)
 |      
 |      Gets element attribute values as a sequence of strings.  The
 |      attributes are returned in an arbitrary order.
 |  
 |  xpath(...)
 |      xpath(self, _path, namespaces=None, extensions=None, smart_strings=True, **_variables)
 |      
 |      Evaluate an xpath expression using the element as context node.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from lxml.etree._Element:
 |  
 |  attrib
 |      Element attribute dictionary. Where possible, use get(), set(),
 |      keys(), values() and items() to access element attributes.
 |  
 |  base
 |      The base URI of the Element (xml:base or HTML base URL).
 |      None if the base URI is unknown.
 |      
 |      Note that the value depends on the URL of the document that
 |      holds the Element if there is no xml:base attribute on the
 |      Element or its ancestors.
 |      
 |      Setting this property will set an xml:base attribute on the
 |      Element, regardless of the document type (XML or HTML).
 |  
 |  nsmap
 |      Namespace prefix->URI mapping known in the context of this
 |      Element.  This includes all namespace declarations of the
 |      parents.
 |      
 |      Note that changing the returned dict has no effect on the Element.
 |  
 |  prefix
 |      Namespace prefix or None.
 |  
 |  sourceline
 |      Original line number as found by the parser or None if unknown.
 |  
 |  tag
 |      Element tag
 |  
 |  tail
 |      Text after this element's end tag, but before the next sibling
 |      element's start tag. This is either a string or the value None, if
 |      there was no text.
 |  
 |  text
 |      Text before the first subelement. This is either a string or 
 |      the value None, if there was no text.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from HtmlMixin:
 |  
 |  cssselect(self, expr, translator='html')
 |      Run the CSS expression on this element and its children,
 |      returning a list of the results.
 |      
 |      Equivalent to lxml.cssselect.CSSSelect(expr, translator='html')(self)
 |      -- note that pre-compiling the expression can provide a substantial
 |      speedup.
 |  
 |  drop_tag(self)
 |      Remove the tag, but not its children or text.  The children and text
 |      are merged into the parent.
 |      
 |      Example::
 |      
 |          >>> h = fragment_fromstring('<div>Hello <b>World!</b></div>')
 |          >>> h.find('.//b').drop_tag()
 |          >>> print(tostring(h, encoding='unicode'))
 |          <div>Hello World!</div>
 |  
 |  drop_tree(self)
 |      Removes this element from the tree, including its children and
 |      text.  The tail text is joined to the previous element or
 |      parent.
 |  
 |  find_class(self, class_name)
 |      Find any elements with the given class name.
 |  
 |  find_rel_links(self, rel)
 |      Find any links like ``<a rel="{rel}">...</a>``; returns a list of elements.
 |  
 |  get_element_by_id(self, id, *default)
 |      Get the first element in a document with the given id.  If none is
 |      found, return the default argument if provided or raise KeyError
 |      otherwise.
 |      
 |      Note that there can be more than one element with the same id,
 |      and this isn't uncommon in HTML documents found in the wild.
 |      Browsers return only the first match, and this function does
 |      the same.
 |  
 |  iterlinks(self)
 |      Yield (element, attribute, link, pos), where attribute may be None
 |      (indicating the link is in the text).  ``pos`` is the position
 |      where the link occurs; often 0, but sometimes something else in
 |      the case of links in stylesheets or style tags.
 |      
 |      Note: <base href> is *not* taken into account in any way.  The
 |      link you get is exactly the link in the document.
 |      
 |      Note: multiple links inside of a single text string or
 |      attribute value are returned in reversed order.  This makes it
 |      possible to replace or delete them from the text string value
 |      based on their reported text positions.  Otherwise, a
 |      modification at one text position can change the positions of
 |      links reported later on.
 |  
 |  make_links_absolute(self, base_url=None, resolve_base_href=True, handle_failures=None)
 |      Make all links in the document absolute, given the
 |      ``base_url`` for the document (the full URL where the document
 |      came from), or if no ``base_url`` is given, then the ``.base_url``
 |      of the document.
 |      
 |      If ``resolve_base_href`` is true, then any ``<base href>``
 |      tags in the document are used *and* removed from the document.
 |      If it is false then any such tag is ignored.
 |      
 |      If ``handle_failures`` is None (default), a failure to process
 |      a URL will abort the processing.  If set to 'ignore', errors
 |      are ignored.  If set to 'discard', failing URLs will be removed.
 |  
 |  resolve_base_href(self, handle_failures=None)
 |      Find any ``<base href>`` tag in the document, and apply its
 |      values to all links found in the document.  Also remove the
 |      tag once it has been applied.
 |      
 |      If ``handle_failures`` is None (default), a failure to process
 |      a URL will abort the processing.  If set to 'ignore', errors
 |      are ignored.  If set to 'discard', failing URLs will be removed.
 |  
 |  rewrite_links(self, link_repl_func, resolve_base_href=True, base_href=None)
 |      Rewrite all the links in the document.  For each link
 |      ``link_repl_func(link)`` will be called, and the return value
 |      will replace the old link.
 |      
 |      Note that links may not be absolute (unless you first called
 |      ``make_links_absolute()``), and may be internal (e.g.,
 |      ``'#anchor'``).  They can also be values like
 |      ``'mailto:email'`` or ``'javascript:expr'``.
 |      
 |      If you give ``base_href`` then all links passed to
 |      ``link_repl_func()`` will take that into account.
 |      
 |      If the ``link_repl_func`` returns None, the attribute or
 |      tag text will be removed completely.
 |  
 |  text_content(self)
 |      Return the text content of the tag (and the text in any children).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from HtmlMixin:
 |  
 |  base_url
 |      Returns the base URL, given when the page was parsed.
 |      
 |      Use with ``urlparse.urljoin(el.base_url, href)`` to get
 |      absolute URLs.
 |  
 |  body
 |      Return the <body> element.  Can be called from a child element
 |      to get the document's head.
 |  
 |  forms
 |      Return a list of all the forms
 |  
 |  head
 |      Returns the <head> element.  Can be called from a child
 |      element to get the document's head.
 |  
 |  label
 |      Get or set any <label> element associated with this element.