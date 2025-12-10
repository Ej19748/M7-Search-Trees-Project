class ScheduleItem:
  """Represents a single course schedule entry."""

  def __init__(self, subject, catalog, section, component, session,
               min_units, units, tot_enrl, cap_enrl, instructor,
               capacity, room, mtg_start, mtg_end, days,
               start_date, end_date, term, campus, class_nbr, total_credits):
      self.subject = subject
      self.catalog = catalog
      self.section = section
      self.component = component
      self.session = session
      self.min_units = min_units
      self.units = units
      self.tot_enrl = tot_enrl
      self.cap_enrl = cap_enrl
      self.instructor = instructor
      self.capacity = capacity
      self.room = room
      self.mtg_start = mtg_start
      self.mtg_end = mtg_end
      self.days = days
      self.start_date = start_date
      self.end_date = end_date
      self.term = term
      self.campus = campus
      self.class_nbr = class_nbr
      self.total_credits = total_credits

  def get_key(self):
      """Return unique key for this schedule item (class number)."""
      return self.class_nbr

  def get_course_id(self):
      """Return course identifier (Subject + Catalog)."""
      return f"{self.subject} {self.catalog}"

  def __str__(self):
      """Return string representation of schedule item."""
      return (f"{self.subject} {self.catalog} {self.section} | "
              f"{self.component} | {self.instructor} | "
              f"{self.days} {self.mtg_start}-{self.mtg_end} | "
              f"Room: {self.room} | Enrolled: {self.tot_enrl}/{self.cap_enrl}")

  def __repr__(self):
      return f"ScheduleItem({self.subject}, {self.catalog}, {self.section})"

  def to_dict(self):
      """Convert schedule item to dictionary."""
      return {
          'Subject': self.subject,
          'Catalog': self.catalog,
          'Section': self.section,
          'Component': self.component,
          'Session': self.session,
          'MinUnits': self.min_units,
          'Units': self.units,
          'TotEnrl': self.tot_enrl,
          'CapEnrl': self.cap_enrl,
          'Instructor': self.instructor,
          'Capacity': self.capacity,
          'Room': self.room,
          'Mtg Start': self.mtg_start,
          'Mtg End': self.mtg_end,
          'Days': self.days,
          'Start Date': self.start_date,
          'End Date': self.end_date,
          'Term': self.term,
          'Campus': self.campus,
          'Class Nbr': self.class_nbr,
          'Total Credits': self.total_credits
      }

  @classmethod
  def from_dict(cls, row):
      """Create ScheduleItem from dictionary (e.g., from csv.DictReader)."""
      return cls(
          subject=row.get('Subject', ''),
          catalog=row.get('Catalog', ''),
          section=row.get('Section', ''),
          component=row.get('Component', ''),
          session=row.get('Session', ''),
          min_units=row.get('MinUnits', ''),
          units=row.get('Units', ''),
          tot_enrl=row.get('TotEnrl', ''),
          cap_enrl=row.get('CapEnrl', ''),
          instructor=row.get('Instructor', ''),
          capacity=row.get('Capacity', ''),
          room=row.get('Room', ''),
          mtg_start=row.get('Mtg Start', ''),
          mtg_end=row.get('Mtg End', ''),
          days=row.get('Days', ''),
          start_date=row.get('Start Date', ''),
          end_date=row.get('End Date', ''),
          term=row.get('Term', ''),
          campus=row.get('Campus', ''),
          class_nbr=row.get('Class Nbr', ''),
          total_credits=row.get('Total Credits', '')
      )
