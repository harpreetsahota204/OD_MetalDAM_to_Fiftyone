import fiftyone as fo

def download_dataset():
    """
    Download the OD_MetalDAM Dataset from source
    """
    pass

def crop_dataset():
    """
    Crop images from  1280x895 to 1024x703 and remove the information band at the bottom
    and save to disk
    """
    pass

def sql_to_csv():
    """
    Parse MetalDAM_metadata.sql to csv for easier processing
    """
    pass


def parse_to_fiftyone():
    """
    """

    samples = []
    dataset = fo.Dataset(name="OD_MetalDAM", overwrite=True)

    # parse FO samples

    # probably  need to load csv and parse the metadata


    # load image from disk
    # load colored mask from disk, parse as segmentation with mask_path
    # load uncolored mask from disk, parse as segmentation with mask_path


    dataset.add_samples(samples)
    dataset.compute_metadata()
    dataset.add_dynamic_sample_fields()

    pass