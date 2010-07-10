/*
  pygame - Python Game Library
  Copyright (C) 2000-2001  Pete Shinners, 2006 Rene Dudfield,
                2007-2010 Marcus von Appen

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Library General Public
  License as published by the Free Software Foundation; either
  version 2 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Library General Public License for more details.

  You should have received a copy of the GNU Library General Public
  License along with this library; if not, write to the Free
  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

*/

#include "surface_blit.h"

CREATE_BLITTER(blend_rgba_add, D_BLEND_RGBA_ADD(tmp,sR,sG,sB,sA,dR,dG,dB,dA),,,)
CREATE_BLITTER(blend_rgba_sub, D_BLEND_RGBA_SUB(tmp2,sR,sG,sB,sA,dR,dG,dB,dA),,,)
CREATE_BLITTER(blend_rgba_mul, D_BLEND_RGBA_MULT(sR,sG,sB,sA,dR,dG,dB,dA),,,)
CREATE_BLITTER(blend_rgba_min, D_BLEND_RGBA_MIN(sR,sG,sB,sA,dR,dG,dB,dA),,,)
CREATE_BLITTER(blend_rgba_max, D_BLEND_RGBA_MAX(sR,sG,sB,sA,dR,dG,dB,dA),,,)
CREATE_BLITTER(blend_rgba_xor, D_BLEND_RGBA_XOR(sR,sG,sB,sA,dR,dG,dB,dA),,,)
CREATE_BLITTER(blend_rgba_and, D_BLEND_RGBA_AND(sR,sG,sB,sA,dR,dG,dB,dA),,,)
CREATE_BLITTER(blend_rgba_or, D_BLEND_RGBA_OR(sR,sG,sB,sA,dR,dG,dB,dA),,,)
CREATE_BLITTER(blend_rgba_diff, D_BLEND_RGBA_DIFF(sR,sG,sB,sA,dR,dG,dB,dA),,,)
CREATE_BLITTER(blend_rgba_screen, D_BLEND_RGBA_SCREEN(sR,sG,sB,sA,dR,dG,dB,dA),,,)
CREATE_BLITTER(blend_rgba_avg, D_BLEND_RGBA_AVG(sR,sG,sB,sA,dR,dG,dB,dA),,,)
