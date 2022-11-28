import React from "react";
import PropTypes from "prop-types";
import { fileToDataUrl } from "../helper.js";

import {
  Button,
  Box,
  DialogTitle,
  CircularProgress,
  DialogActions,
} from "@mui/material/";
import PhotoCameraIcon from "@mui/icons-material/PhotoCamera";

export default function EditProfPicDialog({ submit }) {
  const [selectedImage, setSelectedImage] = React.useState(null);
  const [imageUrl, setImageUrl] = React.useState(null);

  React.useEffect(() => {
    if (selectedImage) {
      if (selectedImage !== null) {
        // returns a promise, need to capture whats in it
        fileToDataUrl(selectedImage).then((body) => {
          if (body.error) {
            alert(body.error);
          } else {
            setImageUrl(body);
          }
        });
      }
    }
  }, [selectedImage]);

  const handleSubmit = () => {
    submit(imageUrl);
  };

  const titleStyle = { margin: "20px 5px" };
  const buttonStyle = {
    marginLeft: "25px",
    marginBottom: "50px",
    marginRight: "25px",
  };
  const butStyle = { marginBottom: "50px", marginTop: "30px" };

  return (
    <>
      <DialogTitle style={titleStyle}>Edit Profile Picture</DialogTitle>
      <input
        accept="image/*"
        type="file"
        id="select-image"
        style={{ display: "none" }}
        onChange={(e) => setSelectedImage(e.target.files[0])}
      />
      <label htmlFor="select-image">
        <Button
          style={buttonStyle}
          variant="outlined"
          color="primary"
          component="span"
          endIcon={<PhotoCameraIcon />}
        >
          Upload Image
        </Button>
      </label>
      {imageUrl && selectedImage && (
        <Box mt={2} textAlign="center">
          <div>Image Preview:</div>
          <img src={imageUrl} alt={selectedImage.name} height="100px" />
          <br />
          <Button
            style={butStyle}
            variant="outlined"
            onClick={() => setSelectedImage(null)}
          >
            Remove Image
          </Button>
          <br />
          <DialogActions>
            <Button
              style={buttonStyle}
              variant="contained"
              onClick={handleSubmit}
            >
              Submit
            </Button>
          </DialogActions>
        </Box>
      )}
      {selectedImage && imageUrl === null && <CircularProgress />}
    </>
  );
}

EditProfPicDialog.propTypes = {
  submit: PropTypes.string,
};
