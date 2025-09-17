import fiftyone as fo

def parse_to_fiftyone():
    """
    """

    samples = []
    dataset = fo.Dataset(name="OD_MetalDAM", overwrite=True)

    # parse FO samples


    # load image from disk
    # load colored mask from disk, parse as segmentation with mask_path
    # load uncolored mask from disk, parse as segmentation with mask_path


    dataset.add_samples(samples)
    dataset.compute_metadata()
    dataset.add_dynamic_sample_fields()

    pass