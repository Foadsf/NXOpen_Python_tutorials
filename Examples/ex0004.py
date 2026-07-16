# ex0004.py
import NXOpen
import NXOpen.Features

def yacht_builder(session=NXOpen.Session.GetSession(),
                  work_part=NXOpen.Session.GetSession().Parts.Work,
                  yacht_length=25000.0,
                  yacht_width=6000.0,
                  hull_depth=3000.0):
    mark_id = session.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Parametric Yacht")
    mm = work_part.UnitCollection.FindObject("MilliMeter")

    # Expressions for the hull's dimensions
    work_part.Expressions.CreateSystemExpressionWithUnits(f"Yacht_Length={yacht_length}", mm)
    work_part.Expressions.CreateSystemExpressionWithUnits(f"Yacht_Width={yacht_width}", mm)
    work_part.Expressions.CreateSystemExpressionWithUnits(f"Hull_Depth={hull_depth}", mm)

    # Hull
    hull_builder = work_part.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    hull_builder.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    hull_origin = NXOpen.Point3d(0.0, 0.0, 0.0)
    hull_builder.SetOriginAndLengths(hull_origin, "Yacht_Length", "Yacht_Width", "Hull_Depth")
    hull_feature = hull_builder.Commit()
    hull_builder.Destroy()

    # Cabin
    cabin_builder = work_part.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    cabin_builder.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    cabin_origin = NXOpen.Point3d(float(yacht_length) / 4, 1000.0, float(hull_depth))
    cabin_builder.SetOriginAndLengths(cabin_origin, "Yacht_Length / 2", "Yacht_Width - 2000", "Hull_Depth * 3/4")
    cabin_feature = cabin_builder.Commit()
    cabin_builder.Destroy()

    return hull_feature, cabin_feature, mark_id

def main():
    yacht_builder()

if __name__ == '__main__':
    main()