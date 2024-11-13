import json

class Image:
    def __init__(self, date_taken: str, image_url: str, s3_key: str, s3_bucket_name: str):
        """
        Constructor for the Image class.
        
        :param date_taken: Date when the image was taken, as a string.
        :param image_url: URL of the image.
        :param s3_key: S3 key for the image in the bucket.
        :param s3_bucket_name: S3 bucket name where the image is stored.
        """
        self._date_taken = date_taken
        self._image_url = image_url
        self._s3_key = s3_key
        self._s3_bucket_name = s3_bucket_name

    # Setters
    def set_date_taken(self, date: str):
        self._date_taken = date

    def set_image_url(self, url: str):
        self._image_url = url

    def set_s3_key(self, s3_key: str):
        self._s3_key = s3_key

    def set_s3_bucket_name(self, name: str):
        self._s3_bucket_name = name

    # Getters
    def get_date_taken(self) -> str:
        return self._date_taken

    def get_image_url(self) -> str:
        return self._image_url

    def get_s3_key(self) -> str:
        return self._s3_key

    def get_s3_bucket_name(self) -> str:
        return self._s3_bucket_name

    # JSON Serialization
    def to_json(self) -> dict:
        """
        Converts the Image instance to a JSON-compatible dictionary.
        
        :return: Dictionary with image details.
        """
        return {
            "dateTaken": self._date_taken,
            "imageURL": self._image_url,
            "s3_key": self._s3_key,
            "s3_bucket_name": self._s3_bucket_name
        }

    @classmethod
    def from_json(cls, data: dict) -> 'Image':
        """
        Creates an Image instance from a JSON-compatible dictionary.
        
        :param data: Dictionary with image details.
        :return: A new Image instance.
        """
        return cls(
            date_taken=data.get("dateTaken", ""),
            image_url=data.get("imageURL", ""),
            s3_key=data.get("s3_key", ""),
            s3_bucket_name=data.get("s3_bucket_name", "")
        )

    def __repr__(self) -> str:
        return (f"Image(date_taken='{self._date_taken}', "
                f"image_url='{self._image_url}', "
                f"s3_key='{self._s3_key}', "
                f"s3_bucket_name='{self._s3_bucket_name}')")