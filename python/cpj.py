# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Cpj(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.cpj_header = Cpj.CpjHeader(self._io, self, self._root)

    class CpjVector(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_u4le()
            self.y = self._io.read_u4le()
            self.z = self._io.read_u4le()


    class CpjQuat(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.v = Cpj.CpjVector(self._io, self, self._root)
            self.s = self._io.read_f4le()


    class CpjHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.riff_magic = (self._io.read_bytes(4)).decode(u"utf-8")
            self.len_file = self._io.read_u4le()
            self._raw_body = self._io.read_bytes(self.len_file)
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = Cpj.CpjHeader.Body(_io__raw_body, self, self._root)

        class Body(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.form_magic = (self._io.read_bytes(4)).decode(u"utf-8")
                self.chunks = []
                i = 0
                while not self._io.is_eof():
                    self.chunks.append(Cpj.CpjHeader.Body.Chunk(self._io, self, self._root))
                    i += 1


            class Lodb(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.special_header = Cpj.CpjHeader.Body.SpecialHeader(self._io, self, self._root)
                    self.num_levels = self._io.read_u4le()
                    self.ofs_levels = self._io.read_u4le()
                    self.num_triangles = self._io.read_u4le()
                    self.ofs_triangles = self._io.read_u4le()
                    self.num_vert_relay = self._io.read_u4le()
                    self.ofs_vert_relay = self._io.read_u4le()
                    self.data = self._io.read_bytes_full()

                class Triangle(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.srf_tri_index = self._io.read_u4le()
                        self.vert_index = self._io.read_u2le()
                        self.uv_index = self._io.read_u2le()


                class Level(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.detail = self._io.read_f4le()
                        self.num_triangles = self._io.read_u4le()
                        self.num_vert_relay = self._io.read_u4le()
                        self.first_triangle = self._io.read_u4le()
                        self.first_vert_relay = self._io.read_u4le()


                @property
                def levels(self):
                    if hasattr(self, '_m_levels'):
                        return self._m_levels if hasattr(self, '_m_levels') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_levels)
                    self._m_levels = [None] * (self.num_levels)
                    for i in range(self.num_levels):
                        self._m_levels[i] = Cpj.CpjHeader.Body.Lodb.Level(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_levels if hasattr(self, '_m_levels') else None

                @property
                def triangles(self):
                    if hasattr(self, '_m_triangles'):
                        return self._m_triangles if hasattr(self, '_m_triangles') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_triangles)
                    self._m_triangles = [None] * (self.num_triangles)
                    for i in range(self.num_triangles):
                        self._m_triangles[i] = Cpj.CpjHeader.Body.Lodb.Triangle(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_triangles if hasattr(self, '_m_triangles') else None

                @property
                def vertex_relay(self):
                    if hasattr(self, '_m_vertex_relay'):
                        return self._m_vertex_relay if hasattr(self, '_m_vertex_relay') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_vert_relay)
                    self._m_vertex_relay = [None] * (self.num_vert_relay)
                    for i in range(self.num_vert_relay):
                        self._m_vertex_relay[i] = self._io.read_u2le()

                    self._io.seek(_pos)
                    return self._m_vertex_relay if hasattr(self, '_m_vertex_relay') else None


            class Macb(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.special_header = Cpj.CpjHeader.Body.SpecialHeader(self._io, self, self._root)
                    self.num_sections = self._io.read_u4le()
                    self.ofs_sections = self._io.read_u4le()
                    self.num_commands = self._io.read_u4le()
                    self.ofs_commands = self._io.read_u4le()
                    self.data = (self._io.read_bytes_full()).decode(u"utf-8")

                class Section(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.ofs_name = self._io.read_u4le()
                        self.num_commands = self._io.read_u4le()
                        self.first_command = self._io.read_u4le()


                class Command(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.offset = self._io.read_u4le()

                    @property
                    def command_string(self):
                        if hasattr(self, '_m_command_string'):
                            return self._m_command_string if hasattr(self, '_m_command_string') else None

                        _pos = self._io.pos()
                        self._io.seek(self.offset)
                        self._m_command_string = (self._io.read_bytes(12)).decode(u"utf-8")
                        self._io.seek(_pos)
                        return self._m_command_string if hasattr(self, '_m_command_string') else None


                @property
                def sections(self):
                    if hasattr(self, '_m_sections'):
                        return self._m_sections if hasattr(self, '_m_sections') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_sections)
                    self._m_sections = [None] * (self.num_sections)
                    for i in range(self.num_sections):
                        self._m_sections[i] = Cpj.CpjHeader.Body.Macb.Section(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_sections if hasattr(self, '_m_sections') else None

                @property
                def commands(self):
                    if hasattr(self, '_m_commands'):
                        return self._m_commands if hasattr(self, '_m_commands') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_commands)
                    self._m_commands = [None] * (self.num_commands)
                    for i in range(self.num_commands):
                        self._m_commands[i] = Cpj.CpjHeader.Body.Macb.Command(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_commands if hasattr(self, '_m_commands') else None


            class Chunk(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.header = Cpj.CpjHeader.Body.ChunkHeader(self._io, self, self._root)
                    _on = self.header.magic
                    if _on == u"FRMB":
                        self._raw_data = self._io.read_bytes(self.header.len_file)
                        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                        self.data = Cpj.CpjHeader.Body.Frmb(_io__raw_data, self, self._root)
                    elif _on == u"SKLB":
                        self._raw_data = self._io.read_bytes(self.header.len_file)
                        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                        self.data = Cpj.CpjHeader.Body.Sklb(_io__raw_data, self, self._root)
                    elif _on == u"SEQB":
                        self._raw_data = self._io.read_bytes(self.header.len_file)
                        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                        self.data = Cpj.CpjHeader.Body.Seqb(_io__raw_data, self, self._root)
                    elif _on == u"MACB":
                        self._raw_data = self._io.read_bytes(self.header.len_file)
                        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                        self.data = Cpj.CpjHeader.Body.Macb(_io__raw_data, self, self._root)
                    elif _on == u"LODB":
                        self._raw_data = self._io.read_bytes(self.header.len_file)
                        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                        self.data = Cpj.CpjHeader.Body.Lodb(_io__raw_data, self, self._root)
                    elif _on == u"GEOB":
                        self._raw_data = self._io.read_bytes(self.header.len_file)
                        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                        self.data = Cpj.CpjHeader.Body.Geob(_io__raw_data, self, self._root)
                    elif _on == u"SRFB":
                        self._raw_data = self._io.read_bytes(self.header.len_file)
                        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                        self.data = Cpj.CpjHeader.Body.Srfb(_io__raw_data, self, self._root)
                    else:
                        self.data = self._io.read_bytes(self.header.len_file)
                    self.pad_byte = self._io.read_bytes((self.header.len_file % 2))


            class Sklb(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.special_header = Cpj.CpjHeader.Body.SpecialHeader(self._io, self, self._root)
                    self.num_bones = self._io.read_u4le()
                    self.ofs_bones = self._io.read_u4le()
                    self.num_verts = self._io.read_u4le()
                    self.ofs_verts = self._io.read_u4le()
                    self.num_weights = self._io.read_u4le()
                    self.ofs_weights = self._io.read_u4le()
                    self.num_mounts = self._io.read_u4le()
                    self.ofs_mounts = self._io.read_u4le()

                class SkeletalVert(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.num_weights = self._io.read_u2le()
                        self.first_weight = self._io.read_u2le()


                class Bone(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.ofs_name = self._io.read_u4le()
                        self.parent_index = self._io.read_u4le()
                        self.base_scale = Cpj.CpjVector(self._io, self, self._root)
                        self.base_rotate = Cpj.CpjQuat(self._io, self, self._root)
                        self.base_translate = Cpj.CpjVector(self._io, self, self._root)
                        self.length = self._io.read_f4le()


                class Weight(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.bone_index = self._io.read_u4le()
                        self.weight_factor = self._io.read_f4le()
                        self.ofs_pos = Cpj.CpjVector(self._io, self, self._root)


                class Mount(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.ofs_name = self._io.read_u4le()
                        self.bone_index = self._io.read_u4le()
                        self.base_scale = Cpj.CpjVector(self._io, self, self._root)
                        self.base_rotate = Cpj.CpjQuat(self._io, self, self._root)
                        self.base_translate = Cpj.CpjVector(self._io, self, self._root)


                @property
                def bones(self):
                    if hasattr(self, '_m_bones'):
                        return self._m_bones if hasattr(self, '_m_bones') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_bones)
                    self._m_bones = [None] * (self.num_bones)
                    for i in range(self.num_bones):
                        self._m_bones[i] = Cpj.CpjHeader.Body.Sklb.Bone(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_bones if hasattr(self, '_m_bones') else None

                @property
                def verts(self):
                    if hasattr(self, '_m_verts'):
                        return self._m_verts if hasattr(self, '_m_verts') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_verts)
                    self._m_verts = [None] * (self.num_verts)
                    for i in range(self.num_verts):
                        self._m_verts[i] = Cpj.CpjHeader.Body.Sklb.SkeletalVert(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_verts if hasattr(self, '_m_verts') else None

                @property
                def weights(self):
                    if hasattr(self, '_m_weights'):
                        return self._m_weights if hasattr(self, '_m_weights') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_weights)
                    self._m_weights = [None] * (self.num_weights)
                    for i in range(self.num_weights):
                        self._m_weights[i] = Cpj.CpjHeader.Body.Sklb.Weight(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_weights if hasattr(self, '_m_weights') else None

                @property
                def mounts(self):
                    if hasattr(self, '_m_mounts'):
                        return self._m_mounts if hasattr(self, '_m_mounts') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_mounts)
                    self._m_mounts = [None] * (self.num_mounts)
                    for i in range(self.num_mounts):
                        self._m_mounts[i] = Cpj.CpjHeader.Body.Sklb.Mount(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_mounts if hasattr(self, '_m_mounts') else None


            class Geob(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.special_header = Cpj.CpjHeader.Body.SpecialHeader(self._io, self, self._root)
                    self.num_vertices = self._io.read_u4le()
                    self.ofs_vertices = self._io.read_u4le()
                    self.num_edges = self._io.read_u4le()
                    self.ofs_edges = self._io.read_u4le()
                    self.num_tris = self._io.read_u4le()
                    self.ofs_tris = self._io.read_u4le()
                    self.num_mounts = self._io.read_u4le()
                    self.ofs_mounts = self._io.read_u4le()
                    self.num_obj_links = self._io.read_u4le()
                    self.ofs_obj_links = self._io.read_u4le()
                    self.data = (self._io.read_bytes_full()).decode(u"utf-8")

                class Vertice(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.flags = self._io.read_u1()
                        self.group_index = self._io.read_u1()
                        self.reserved = self._io.read_u2le()
                        self.num_edge_links = self._io.read_u2le()
                        self.num_tri_links = self._io.read_u2le()
                        self.first_edge_link = self._io.read_u4le()
                        self.first_tri_link = self._io.read_u4le()
                        self.ref_position = Cpj.CpjVector(self._io, self, self._root)


                class Edge(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.head_vertex = self._io.read_u2le()
                        self.tail_vertex = self._io.read_u2le()
                        self.inverted_edge = self._io.read_u2le()
                        self.num_tri_links = self._io.read_u2le()
                        self.first_tri_link = self._io.read_u4le()


                class Tri(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.edge_ring_0 = self._io.read_u2le()
                        self.edge_ring_1 = self._io.read_u2le()
                        self.edge_ring_2 = self._io.read_u2le()
                        self.reserved = self._io.read_u2le()


                @property
                def vertices(self):
                    if hasattr(self, '_m_vertices'):
                        return self._m_vertices if hasattr(self, '_m_vertices') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_vertices)
                    self._m_vertices = [None] * (self.num_vertices)
                    for i in range(self.num_vertices):
                        self._m_vertices[i] = Cpj.CpjHeader.Body.Geob.Vertice(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_vertices if hasattr(self, '_m_vertices') else None

                @property
                def edges(self):
                    if hasattr(self, '_m_edges'):
                        return self._m_edges if hasattr(self, '_m_edges') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_edges)
                    self._m_edges = [None] * (self.num_edges)
                    for i in range(self.num_edges):
                        self._m_edges[i] = Cpj.CpjHeader.Body.Geob.Edge(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_edges if hasattr(self, '_m_edges') else None


            class Srfb(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.special_header = Cpj.CpjHeader.Body.SpecialHeader(self._io, self, self._root)
                    self.num_textures = self._io.read_u4le()
                    self.ofs_textures = self._io.read_u4le()
                    self.num_tris = self._io.read_u4le()
                    self.ofs_tris = self._io.read_u4le()
                    self.num_uv = self._io.read_u4le()
                    self.ofs_uv = self._io.read_u4le()

                class Texture(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.ofs_name = self._io.read_u4le()
                        self.ofs_ref_name = self._io.read_u4le()


                class Tri(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.uv_index = self._io.read_u2le()
                        self.tex_index = self._io.read_u1()
                        self.reserved = self._io.read_u1()
                        self.flags = self._io.read_u4le()
                        self.smooth_group = self._io.read_u1()
                        self.alpha_level = self._io.read_u1()
                        self.glaze_tex_index = self._io.read_u1()
                        self.glaze_func = self._io.read_u1()


                class Uv(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.u = self._io.read_f4le()
                        self.v = self._io.read_f4le()


                @property
                def textures(self):
                    if hasattr(self, '_m_textures'):
                        return self._m_textures if hasattr(self, '_m_textures') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_textures)
                    self._m_textures = [None] * (self.num_textures)
                    for i in range(self.num_textures):
                        self._m_textures[i] = Cpj.CpjHeader.Body.Srfb.Texture(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_textures if hasattr(self, '_m_textures') else None

                @property
                def triangles(self):
                    if hasattr(self, '_m_triangles'):
                        return self._m_triangles if hasattr(self, '_m_triangles') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_tris)
                    self._m_triangles = [None] * (self.num_tris)
                    for i in range(self.num_tris):
                        self._m_triangles[i] = Cpj.CpjHeader.Body.Srfb.Tri(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_triangles if hasattr(self, '_m_triangles') else None

                @property
                def uvs(self):
                    if hasattr(self, '_m_uvs'):
                        return self._m_uvs if hasattr(self, '_m_uvs') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_uv)
                    self._m_uvs = [None] * (self.num_uv)
                    for i in range(self.num_uv):
                        self._m_uvs[i] = Cpj.CpjHeader.Body.Srfb.Uv(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_uvs if hasattr(self, '_m_uvs') else None


            class ChunkHeader(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.magic = (self._io.read_bytes(4)).decode(u"utf-8")
                    self.len_file = self._io.read_u4le()


            class SpecialHeader(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.version = self._io.read_u4le()
                    self.timestamp = self._io.read_u4le()
                    self.ofs_name = self._io.read_u4le()


            class Seqb(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.special_header = Cpj.CpjHeader.Body.SpecialHeader(self._io, self, self._root)
                    self.play_rate = self._io.read_f4le()
                    self.num_frames = self._io.read_u4le()
                    self.ofs_frames = self._io.read_u4le()
                    self.num_events = self._io.read_u4le()
                    self.ofs_events = self._io.read_u4le()
                    self.num_bone_info = self._io.read_u4le()
                    self.ofs_bone_info = self._io.read_u4le()
                    self.num_bone_translate = self._io.read_u4le()
                    self.ofs_bone_translate = self._io.read_u4le()
                    self.num_bone_rotate = self._io.read_u4le()
                    self.num_bone_scale = self._io.read_u4le()
                    self.ofs_bone_scale = self._io.read_u4le()


            class Frmb(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.special_header = Cpj.CpjHeader.Body.SpecialHeader(self._io, self, self._root)
                    self.bb_min = Cpj.CpjVector(self._io, self, self._root)
                    self.bb_max = Cpj.CpjVector(self._io, self, self._root)
                    self.num_frames = self._io.read_u4le()
                    self.ofs_frames = self._io.read_u4le()
                    self.data = self._io.read_bytes_full()

                class Frame(KaitaiStruct):
                    def __init__(self, _io, _parent=None, _root=None):
                        self._io = _io
                        self._parent = _parent
                        self._root = _root if _root else self
                        self._read()

                    def _read(self):
                        self.ofs_frame_name = self._io.read_u4le()
                        self.bb_min = Cpj.CpjVector(self._io, self, self._root)
                        self.bb_max = Cpj.CpjVector(self._io, self, self._root)
                        self.num_groups = self._io.read_u4le()
                        self.ofs_groups = self._io.read_u4le()
                        self.num_verts = self._io.read_u4le()
                        self.ofs_verts = self._io.read_u4le()

                    class FrameBytePos(KaitaiStruct):
                        def __init__(self, _io, _parent=None, _root=None):
                            self._io = _io
                            self._parent = _parent
                            self._root = _root if _root else self
                            self._read()

                        def _read(self):
                            self.group = self._io.read_u1()
                            self.pos = self._io.read_u1()


                    class FrameGroup(KaitaiStruct):
                        def __init__(self, _io, _parent=None, _root=None):
                            self._io = _io
                            self._parent = _parent
                            self._root = _root if _root else self
                            self._read()

                        def _read(self):
                            self.byte_scale = Cpj.CpjVector(self._io, self, self._root)
                            self.byte_translate = Cpj.CpjVector(self._io, self, self._root)



                @property
                def frames(self):
                    if hasattr(self, '_m_frames'):
                        return self._m_frames if hasattr(self, '_m_frames') else None

                    _pos = self._io.pos()
                    self._io.seek(self.ofs_frames)
                    self._m_frames = [None] * (self.num_frames)
                    for i in range(self.num_frames):
                        self._m_frames[i] = Cpj.CpjHeader.Body.Frmb.Frame(self._io, self, self._root)

                    self._io.seek(_pos)
                    return self._m_frames if hasattr(self, '_m_frames') else None





