##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Pdsh(AutotoolsPackage):
    """
    PDSH: a high performance, parallel remote shell utility
    """

    homepage = "https://github.com/grondo/pdsh"
    url      = "https://github.com/grondo/pdsh/archive/pdsh-2.31.tar.gz"

    version('2.31', 'cab34b0ca78f3cf596fd648b265223ed')

    variant('ssh', default=True, description="Build with ssh module")

    variant('static_modules', default=True, description="Build with static modules")

    def configure_args(self):
        args = []
        if '+ssh' in self.spec:
            args.append('--with-ssh')
        if '+static_modules' in self.spec:
            args.append('--enable-static-modules')
        return args
