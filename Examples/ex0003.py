# ex0003.py

import NXOpen
import NXOpen.Features

def cylinder_builder(session=NXOpen.Session.GetSession(), work_part=NXOpen.Session.GetSession().Parts.Work, height=100, diameter=50):
    mark_id = session.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Cylinder")
    cylinder = work_part.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    cylinder.Diameter.SetFormula(str(diameter))
    cylinder.Height.SetFormula(str(height))
    nx_object = cylinder.Commit()
    return nx_object, mark_id

def main(): 

    cylinder_builder(height=40, diameter=100)

if __name__ == '__main__':
    main()