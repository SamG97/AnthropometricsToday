CREATE TABLE public.students_post_1897
(
   "DM_month" integer,
   "DM_day" integer,
   "DM_year" integer,
   "Name" character varying(100), -- in case if any name like Ovuvuevuevue Onyetenyevwe Ugwemubwem Ossas will appear
   "College" character varying(20),
   "Age" integer,
   "Birthplace1" character varying(100), -- in case if any place like Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu will appear
   "Birthplace2" character varying(100),
   "Father_origin" character varying(100),
   "Mother_origin" character varying(100),
   "Skin" integer,
   "Hair_colour" real,
   "Hair_type" integer,
   "Eyes" integer, -- light, medium, or dark
   "Face_type" integer, 
   "Cheekbones" integer,
   "Ears" real,
   "Lobes" integer,
   "Head_length" integer,
   "Head_breadth" integer,
   "Head_height" integer,
   "Nose_length" integer,
   "Nose_breadth" integer,
   "Nose_profile" character varying(100),
   "Face_length" integer,
   "Face_upper" integer,
   "Face_breadth" integer,
   "Face_iobreadth" integer,
   "Face_bibreadth" integer,
   "Height_feet" integer,
   "Height_inches" integer,
   "Height_tenths" integer,
   "True_feet" integer, -- true height
   "True_inches" integer,
   "True_tenths" integer,
   "Span_ft" integer,
   "Span_in" integer,
   "Span_tenths" integer,
   "Weight_stone" integer,
   "Weight_lbs" character varying(20), -- sometimes is is not written properly
   "Weight_oz (rare)" real,
   "Breathing Power" integer, -- cubic inches
   "Pull_archer" integer,
   "Squeeze_right" integer,
   "Squeeze_left" integer,
   "Eye_right" integer,
   "Eye_left" integer,
   "Colour_sense" character varying(10),
   "Ceph_index_1" real,
   "Ceph_index_2" real,
   "Facial_index" real,
   "Nasal_index" real,
   "Upperfacial_index" real,
   "JOL" real,
   "BL" real,
   id serial NOT NULL,
   CONSTRAINT post1897studentkey PRIMARY KEY (id)
)
