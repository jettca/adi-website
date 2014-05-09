from app.mod_media.models import Image
from wtforms import TextField, FieldList, StringField, TextAreaField
from flask.ext.wtf import Form
from wtforms.validators import Regexp, Required, ValidationError

def image_with_same_name(form,field):
    if Image.objects(filename=field.data).count() != 1:
        return ValidationError(
            message="Can't find image `%s` in the database" % field.data)

class CreateBlogPostForm(Form):

    title = TextField('Title', [
        Required(message="Please provide the post title.")])
    slug = TextField('Post Slug', [
        Required(message="Please provide a post slug."),
        Regexp('([0-9]|[a-z]|[A-Z]|-)*', message="Post slug should only contain numbers, letters and dashes.")])
    body = TextAreaField('Post Body', [
        Required(message="Please provide a post body.")],
        default="Type your post here.\n\nRendered in **Markdown**!")
    images = FieldList(StringField('Image', [image_with_same_name]), [Required("add images!")])