meta:
  id: cpj
  endian: le
  
seq:
  - id: cpj_header
    type: cpj_header

types:
  cpj_vector:
    seq:
      - id: x
        type: u4
      - id: y
        type: u4
      - id: z
        type: u4
  cpj_quat:
    seq:
      - id: v
        type: cpj_vector
      - id: s
        type: f4
      
  cpj_header:
    seq:
      - id: riff_magic
        type: str
        encoding: utf-8
        size: 4
      - id: len_file
        type: u4
      - id: body
        type: body
        size: len_file
    types:
      body:
        seq:
          - id: form_magic
            type: str
            encoding: utf-8
            size: 4
          - id: chunks
            type: chunk
            repeat: eos
        types: 
          chunk:
            seq:
              - id: header
                type: chunk_header
              - id: data
                type:
                  switch-on: header.magic
                  cases:
                    '"LODB"': lodb
                    '"MACB"': macb
                    '"GEOB"': geob
                    '"SRFB"': srfb
                    '"SKLB"': sklb
                    '"FRMB"': frmb
                    '"SEQB"': seqb
                size: header.len_file
              - id: pad_byte
                size: header.len_file % 2 # if size is odd, there is 1 padding byte
      
          chunk_header:
            seq:
              - id: magic
                type: str
                size: 4
                encoding: utf-8
              - id: len_file
                type: u4
                
          special_header:
            seq:
              - id: version
                type: u4
              - id: timestamp
                type: u4
              - id: ofs_name
                type: u4
          
          lodb:
            seq:
              - id: special_header
                type: special_header
              - id: num_levels
                type: u4
              - id: ofs_levels
                type: u4
              - id:  num_triangles
                type: u4
              - id: ofs_triangles
                type: u4
              - id: num_vert_relay
                type: u4
              - id: ofs_vert_relay
                type: u4
              - id: data
                size-eos: true
            instances:
              levels:
                pos: ofs_levels
                type: level
                repeat: expr
                repeat-expr: num_levels
              triangles:
                pos: ofs_triangles
                type: triangle
                repeat: expr
                repeat-expr: num_triangles
              vertex_relay:
                pos: ofs_vert_relay
                type: u2
                repeat: expr
                repeat-expr: num_vert_relay
            types:
              triangle:
                seq:
                  - id: srf_tri_index
                    type: u4
                  - id: vert_index
                    type: u2
                  - id: uv_index
                    type: u2
              level:
                seq:
                  - id: detail
                    type: f4
                  - id: num_triangles
                    type: u4
                  - id: num_vert_relay
                    type: u4
                  - id: first_triangle
                    type: u4
                  - id: first_vert_relay
                    type: u4
          
          frmb:
            seq:
              - id: special_header
                type: special_header
              - id: bb_min
                type: cpj_vector
              - id: bb_max
                type: cpj_vector
              - id: num_frames
                type: u4
              - id: ofs_frames
                type: u4
              - id: data
                size-eos: true
            instances:
              frames:
                pos: ofs_frames
                type: frame
                repeat: expr
                repeat-expr: num_frames
            types:
              frame:
                seq:
                  - id: ofs_frame_name
                    type: u4
                  - id: bb_min
                    type: cpj_vector
                  - id: bb_max
                    type: cpj_vector
                  - id: num_groups
                    type: u4
                  - id: ofs_groups
                    type: u4
                  - id: num_verts
                    type: u4
                  - id: ofs_verts
                    type: u4
                # TODO commenting these out until I understand what I'm doing wrong here...
                #instances:
                  #name:
                    #pos: ofs_frame_name
                    #type: str
                    #size: 4
                    #encoding: utf-8
                  #frame_groups:
                    #io: _parent._io
                    #pos: ofs_groups
                    #type: frame_group
                    #repeat: expr
                    #repeat-expr: num_groups
                  #vertex_positions:
                    #io: _parent._io
                    #pos: ofs_verts
                    #repeat: expr
                    #repeat-expr: num_verts
                    #type: 
                      #switch-on: num_groups
                      #cases:
                        #0: cpj_vector # uncompressed
                        #_: frame_byte_pos # compressed
                types:
                  frame_byte_pos:
                    seq:
                      - id: group
                        type: u1
                      - id: pos
                        type: u1
                  frame_group:
                    seq:
                      - id: byte_scale
                        type: cpj_vector
                      - id: byte_translate
                        type: cpj_vector
                    
          
          sklb:
            seq:
              - id: special_header
                type: special_header
              - id: num_bones
                type: u4
              - id: ofs_bones
                type: u4
              - id: num_verts
                type: u4
              - id: ofs_verts
                type: u4
              - id: num_weights
                type: u4
              - id: ofs_weights
                type: u4
              - id: num_mounts
                type: u4
              - id: ofs_mounts
                type: u4
            instances:
              bones:
                pos: ofs_bones
                repeat: expr
                repeat-expr: num_bones
                type: bone
              verts:
                pos: ofs_verts
                repeat: expr
                repeat-expr: num_verts
                type: skeletal_vert
              weights:
                pos: ofs_weights
                type: weight
                repeat: expr
                repeat-expr: num_weights
              mounts:
                pos: ofs_mounts
                type: mount
                repeat: expr
                repeat-expr: num_mounts
            types:
              skeletal_vert:
                seq:
                  - id: num_weights
                    type: u2
                  - id: first_weight
                    type: u2
              bone:
                seq:
                  - id: ofs_name
                    type: u4
                  - id: parent_index
                    type: u4
                  - id: base_scale
                    type: cpj_vector
                  - id: base_rotate
                    type: cpj_quat
                  - id: base_translate
                    type: cpj_vector
                  - id: length
                    type: f4
              weight:
                seq:
                  - id: bone_index
                    type: u4
                  - id: weight_factor
                    type: f4
                  - id: ofs_pos
                    type: cpj_vector
              mount:
                seq:
                  - id: ofs_name
                    type: u4
                  - id: bone_index
                    type: u4
                  - id: base_scale
                    type: cpj_vector
                  - id: base_rotate
                    type: cpj_quat
                  - id: base_translate
                    type: cpj_vector
          
          seqb:
            seq:
              - id: special_header
                type: special_header
              - id: play_rate
                type: f4
              - id: num_frames
                type: u4
              - id: ofs_frames
                type: u4
              - id: num_events
                type: u4
              - id: ofs_events
                type: u4
              - id: num_bone_info
                type: u4
              - id: ofs_bone_info
                type: u4
              - id: num_bone_translate
                type: u4
              - id: ofs_bone_translate
                type: u4
              - id: num_bone_rotate
                type: u4
              - id: num_bone_scale
                type: u4
              - id: ofs_bone_scale
                type: u4
                
          macb:
            seq:
              - id: special_header
                type: special_header
              - id: num_sections
                type: u4
              - id: ofs_sections
                type: u4
              - id: num_commands
                type: u4
              - id: ofs_commands
                type: u4
              - id: data
                type: str
                encoding: utf-8
                size-eos: true
            instances:
              sections:
                pos: ofs_sections
                type: section
                repeat: expr
                repeat-expr: num_sections
              commands:
                pos: ofs_commands
                type: command
                repeat: expr
                repeat-expr: num_commands
            types:
              section:
                seq:
                  - id: ofs_name
                    type: u4
                  - id: num_commands
                    type: u4
                  - id: first_command
                    type: u4
              command:
                seq:
                  - id: offset
                    type: u4
                instances:
                  command_string: # TODO
                    pos: offset
                    type: str
                    encoding: utf-8
                    size: 12
                
          geob:
            seq:
              - id: special_header
                type: special_header
              - id: num_vertices
                type: u4
              - id: ofs_vertices
                type: u4
              - id: num_edges
                type: u4
              - id: ofs_edges
                type: u4
              - id: num_tris
                type: u4
              - id: ofs_tris
                type: u4
              - id: num_mounts
                type: u4
              - id: ofs_mounts
                type: u4
              - id: num_obj_links
                type: u4
              - id: ofs_obj_links
                type: u4
              - id: data
                type: str
                encoding: utf-8
                size-eos: true
            instances:
              vertices:
                pos: ofs_vertices
                type: vertice
                repeat: expr
                repeat-expr: num_vertices
              edges:
                pos: ofs_edges
                type: edge
                repeat: expr
                repeat-expr: num_edges
            types:
              vertice:
                seq:
                  - id: flags
                    type: u1
                  - id: group_index
                    type: u1
                  - id: reserved
                    type: u2
                  - id: num_edge_links
                    type: u2
                  - id: num_tri_links
                    type: u2
                  - id: first_edge_link
                    type: u4
                  - id: first_tri_link
                    type: u4
                  - id: ref_position
                    type: cpj_vector
              edge:
                seq:
                  - id: head_vertex
                    type: u2
                  - id: tail_vertex
                    type: u2
                  - id: inverted_edge
                    type: u2
                  - id: num_tri_links
                    type: u2
                  - id: first_tri_link
                    type: u4
              tri:
                seq:
                  - id: edge_ring_0
                    type: u2
                  - id: edge_ring_1
                    type: u2
                  - id: edge_ring_2
                    type: u2
                  - id: reserved
                    type: u2
                
                
          srfb:
            seq:
              - id: special_header
                type: special_header
              - id: num_textures
                type: u4
              - id: ofs_textures
                type: u4
              - id: num_tris
                type: u4
              - id: ofs_tris
                type: u4
              - id: num_uv
                type: u4
              - id: ofs_uv
                type: u4
            instances:
              textures:
                pos: ofs_textures
                type: texture
                repeat: expr
                repeat-expr: num_textures
              triangles:
                pos: ofs_tris
                type: tri
                repeat: expr
                repeat-expr: num_tris
              uvs:
                pos: ofs_uv
                type: uv
                repeat: expr
                repeat-expr: num_uv
            types:
              texture:
                seq:
                  - id: ofs_name
                    type: u4
                  - id: ofs_ref_name
                    type: u4
              tri:
                seq:
                  - id: uv_index
                    type: u2
                  - id: tex_index
                    type: u1
                  - id: reserved
                    type: u1
                  - id: flags
                    type: u4
                  - id: smooth_group
                    type: u1
                  - id: alpha_level
                    type: u1
                  - id: glaze_tex_index
                    type: u1
                  - id: glaze_func
                    type: u1
              uv:
                seq:
                  - id: u
                    type: f4
                  - id: v
                    type: f4
                
