# Django Adressbook #

Contacts are accessible and synchronized from and with any authorized client on the network as well as via IrDA and Bluetooth.

# Status #

Subproject started 22th of July 2011.

Current status: Under development. Partially ready, but unstable.

# Database #

  * table **Contacts** holds _first name_, _surname_ and _owner_ of contact.
  * table **ContactAtoms** holds information "atoms" for one contact each

Example:
### Contact ###
  * ID = **25**
  * Owner = **1**
  * Firstname = **Max**
  * Surname = **Mustermann**
### Contact Atom ###
  * ID = **13**
  * Contact = **25**
  * Property = **Birthday**
  * Value = **01.01.1985**
  * Comment = **in Berlin**