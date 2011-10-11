# -*- coding: utf-8 -*-

"""
Absolute Salinity (SA) and Preformed Salinity (Sstar)

Functions:
----------
  SA_from_SP(SP, p, lon, lat)
        Absolute Salinity from Practical Salinity
  Sstar_from_SP(SP, p, lon, lat)
        Preformed Salinity from Practical Salinity
  CT_from_t(SA, t, p)
        Conservative Temperature from in-situ temperature

This is part of the python Gibbs Sea Water library
http://code.google.com/p/python-seawater/

"""

from __future__ import division

#from seawater.constants import ?
#from library import delta_SA
from utilities import match_args_return
from conversions import pt0_from_t, CT_from_pt


__all__ = [
           #'SA_from_SP',
           #'Sstar_from_SP',
           'CT_from_t'  # NOTE: previously at conservative_temperature.py
           #'SA_Sstar_from_SP'  # NOTE: Dropped?
           ]


@match_args_return
def CT_from_t(SA, t, p):
    r"""
    Calculates Conservative Temperature of seawater from in situ temperature.

    Parameters
    ----------
    SA : array_like
         Absolute salinity [g kg :sup:`-1`]
    t : array_like
        in situ temperature [:math:`^\circ` C (ITS-90)]
    p : array_like
        pressure [dbar]

    Returns
    -------
    CT : array_like
         Conservative Temperature [:math:`^\circ` C (ITS-90)]

    See Also
    --------
    TODO

    Notes
    -----
    TODO

    Examples
    --------
    >>> import seawater.gibbs as gsw
    >>> SA = [34.7118, 34.8915, 35.0256, 34.8472, 34.7366, 34.7324]
    >>> t = [28.7856, 28.4329, 22.8103, 10.2600, 6.8863, 4.4036]
    >>> p = [10, 50, 125, 250, 600, 1000]
    >>> gsw.CT_from_t(SA, t, p)
    array([ 28.80991983,  28.43922782,  22.78617689,  10.22618927,
             6.82721363,   4.32357575])

    References
    ----------
    .. [1] IOC, SCOR and IAPSO, 2010: The international thermodynamic equation
    of seawater - 2010: Calculation and use of thermodynamic properties.
    Intergovernmental Oceanographic Commission, Manuals and Guides No. 56,
    UNESCO (English), 196 pp. See section 3.3.

    Modifications:
    2010-08-26. David Jackett, Trevor McDougall and Paul Barker
    2010-12-09. Filipe Fernandes, Python translation from gsw toolbox.
    """

    pt0 = pt0_from_t(SA, t, p)
    CT = CT_from_pt(SA, pt0)

    return CT


if __name__ == '__main__':
    import doctest
    doctest.testmod()
