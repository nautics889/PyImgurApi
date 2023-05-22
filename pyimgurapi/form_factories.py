from .utils import MultipartForm, Field, File


def get_album_form(
    image_ids=None,
    delete_hashes=None,
    title=None,
    description=None,
    privacy=None,
    layout=None,
    cover=None,
):
    possible_privacy_values = ("public", "hidden", "secret")
    if privacy is not None and privacy not in possible_privacy_values:
        raise ValueError(
            f"Inappropriate value for `privacy`: '{privacy}', "
            f"currently supported: {possible_privacy_values}"
        )
    possible_layout_reason = ("blog", "grid", "horizontal", "vertical")
    if layout is not None and layout not in possible_layout_reason:
        raise ValueError(
            f"Inappropriate value for `layout`: '{layout}', "
            f"currently supported: {possible_layout_reason}"
        )

    fields = list()
    if image_ids is not None:
        for image_id in image_ids:
            fields.append(Field(field_name="ids[]", value=image_id))
    if delete_hashes is not None:
        for delete_hash in delete_hashes:
            fields.append(
                Field(field_name="deletehashes[]", value=delete_hash)
            )
    if title is not None:
        fields.append(Field(field_name="title", value=title))
    if description is not None:
        fields.append(Field(field_name="description", value=description))
    if privacy is not None:
        fields.append(Field(field_name="privacy", value=privacy))
    if cover is not None:
        fields.append(Field(field_name="cover", value=cover))
    return MultipartForm(fields=fields)


def get_image_form(
    file_obj=None, filename=None, title=None, description=None, album=None
):
    fields = list()
    if title is not None:
        fields.append(Field(field_name="title", value=title))
    if description is not None:
        fields.append(Field(field_name="description", value=description))
    if album is not None:
        fields.append(Field(field_name="album", value=album))

    files = None
    if file_obj and filename:
        file_data = file_obj.read()
        files = [
            File(name=filename, data=file_data, field_name="image"),
        ]
    return MultipartForm(fields=fields, files=files)


def get_comment_form(image_id, comment):
    fields = [
        Field(field_name="image_id", value=image_id),
        Field(field_name="comment", value=comment),
    ]
    return MultipartForm(fields=fields)


def get_comment_report_form(reason=None):
    possible_reason_values = ("1", "2", "3", "4", "5")
    if reason is not None and str(reason) not in possible_reason_values:
        raise ValueError(
            f"Inappropriate value for `reason`: '{reason}', "
            f"currently supported: {possible_reason_values}"
        )
    fields = []
    if reason:
        fields.append(Field(field_name="reason", value=reason))
    return MultipartForm(fields=fields)
