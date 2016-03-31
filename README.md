Fashion Dataset
=======

Used for training machine learning models. It is compiled from a number of other datasets.



## Fashionista Dataset (158,235 images)

Thanks to [Kota Yamaguchi](http://vision.is.tohoku.ac.jp/~kyamagu/) for the fashionista dataset. [Paper](http://www.cs.unc.edu/~hadi/cvpr_2012.pdf)

The fashionista package contains the Fashionista dataset without annotation,
which was collected from chictopia.com in 2011.

The data is stored in a tab-delimited text files in the following
format. Text files are split into chunks. Concatenating them
will recover the full data records in one table.


posts/xxx.txt
-------------

    Post(id, url)

Post represents a blog post in chictopia.com. In Chictopia, bloggers
upload up to 5 photos to a single post. This table keeps the url of
these posts and a unique identifier in the dataset.

Note that a blogger might delete some of the posts since the dataset was collected. It's not guaranteed that all posts are available.

photos/xxx.txt
--------------

    Photo(post_id, url)

Photo represents a picture associated to each post. In the table,
one row keeps a url and the id of the associated post.

garments/xxx.txt
----------------

    Garment(post_id, name)

Garment is meta-data extracted from the post. In each post, bloggers
list up their clothing items from the pre-defined set of clothing
types. This garment table keeps pairs of the id of the post and
extracted garment name.
