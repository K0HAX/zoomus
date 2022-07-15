"""Zoom.us REST API Python Client -- Contact Center component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components import base

class ContactCenterComponentV2(base.BaseComponent):
    def address_book_units_list(self, **kwargs):
        return self.get_request("/contact_center/address_books/units", params=kwargs)

    def address_book_unit_get(self, **kwargs):
        util.require_keys(kwargs, 'unitId')
        return self.get_request("/contact_center/address_books/units/{}".format(kwargs.get("unitId")), params=kwargs)

    def address_books_list(self, **kwargs):
        util.require_keys(kwargs, 'unit_id')
        return self.get_request("/contact_center/address_books", params=kwargs)

    def address_book_get(self, **kwargs):
        util.require_keys(kwargs, 'addressBookId')
        return self.get_request("/contact_center/address_books/{}".format(kwargs.get("addressBookId")), params=kwargs)

    def address_book_contacts_list(self, **kwargs):
        util.require_keys(kwargs, 'addressBookId')
        return self.get_request("/contact_center/address_books/{}/contacts".format(kwargs.get("addressBookId")), params=kwargs)

    def address_book_contact_get(self, **kwargs):
        util.require_keys(kwargs, "addressBookId")
        util.require_keys(kwargs, "contactId")
        return self.get_request("/contact_center/address_books/{addressBookId}/contacts/{contactId}".format(
            addressBookId=kwargs.get("addressBookId"),
            contactId=kwargs.get("contactId")), params=kwargs)

    def address_book_contact_create(self, **kwargs):
        util.require_keys(kwargs, "addressBookId")
        return self.post_request("/contact_center/address_books/{}/contacts".format(kwargs.get("addressBookId")), data=kwargs)

    def address_book_contact_update(self, **kwargs):
        util.require_keys(kwargs, "addressBookId")
        util.require_keys(kwargs, "contactId")
        return self.patch_request("/contact_center/address_books/{addressBookId}/contacts/{contactId}".format(
            addressBookId=kwargs.get("addressBookId"),
            contactId=kwargs.get("contactId")), data=kwargs)

