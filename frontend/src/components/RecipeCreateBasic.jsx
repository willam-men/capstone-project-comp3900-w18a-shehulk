import React from "react";
import {
  Box,
  Button,
  CircularProgress,
  TextField,
  FormControl,
  Select,
  MenuItem,
  Typography,
  IconButton,
} from "@mui/material";
import PhotoCamera from "@mui/icons-material/PhotoCamera";
import DeleteIcon from "@mui/icons-material/Delete";
import { fileToDataUrl } from "../helper.js";
import TagsInput from "./TagsInput.jsx";

export default function RecipeCreateBasic({
  formData,
  setFormData,
  validateData,
}) {
  const [selectedImage, setSelectedImage] = React.useState(null);
  const [imageUrl, setImageUrl] = React.useState(null);

  const [titleError, setTitleError] = React.useState(false);
  const [servingsError, setServingsError] = React.useState(false);
  const [difficultyError, setDifficultyError] = React.useState(false);
  const [cookMins, setCookMins] = React.useState(0);
  const [cookHours, setCookHours] = React.useState(0);
  const [prepMins, setPrepMins] = React.useState(0);
  const [prepHours, setPrepHours] = React.useState(0);

  const difficultyOptions = ["Easy", "Medium", "Hard"];
  const hoursOptions = Array.from({ length: 6 }, (_, index) => index);
  const minsOptions = Array.from({ length: 13 }, (_, index) => 5 * index);

  React.useEffect(() => {
    if (formData.selectedImage !== null) {
      setSelectedImage(formData.selectedImage);
    }
    if (formData.imageUrl !== null) {
      setImageUrl(formData.imageUrl);
    }
    if (formData.cookMins !== 0) {
      setCookMins(formData.cookMins);
    }
    if (formData.cookHours !== 0) {
      setCookHours(formData.cookHours);
    }
    if (formData.prepMins !== 0) {
      setPrepMins(formData.prepMins);
    }
    if (formData.prepHours !== 0) {
      setPrepHours(formData.prepHours);
    }
  }, [formData]);

  React.useEffect(() => {
    setFormData({
      ...formData,
      prepMins: prepMins,
      prepHours: prepHours,
      cookMins: cookMins,
      cookHours: cookHours,
      imageUrl: imageUrl,
    });
  }, [
    setFormData,
    formData,
    cookMins,
    cookHours,
    prepMins,
    prepHours,
    imageUrl,
  ]);

  React.useEffect(() => {
    if (validateData === true) {
      if (!formData.title) {
        setTitleError(true);
      } else {
        setTitleError(false);
      }
      if (!formData.servings) {
        setServingsError(true);
      } else {
        setServingsError(false);
      }
      if (!formData.difficulty) {
        setDifficultyError(true);
      } else {
        setDifficultyError(false);
      }
    }
  }, [validateData, formData.title, formData.servings, formData.difficulty]);

  const setImage = (file) => {
    setSelectedImage(file);
    setFormData({
      ...formData,
      selectedImage: file,
    });
  };

  const removeImage = () => {
    setSelectedImage(null);
    setImageUrl(null);
    setFormData({
      ...formData,
      selectedImage: null,
      imageUrl: null,
    });
  };

  React.useEffect(() => {
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
  }, [selectedImage, setImageUrl]);

  const handleChangeServings = (e) => {
    if (e.target.value > 0) {
      setFormData({
        ...formData,
        servings: e.target.value,
      });
    }
  };

  const formStyle = { width: "100%" };
  const divStyle = {
    display: "grid",
    alignItems: "start",
    marginBottom: "30px",
  };
  const selectStyle = { marginBottom: "30px", width: "20%", float: "left" };
  const labelStyle = { textAlign: "left" };
  const flexStyle = {
    display: "flex",
    flexDirection: "row",
    justfyContent: "flexStart",
    alignItems: "center",
  };
  const timeStyle = { minWidth: "80px" };
  const buttonStyle = {
    marginRight: "30px",
    width: "150px",
    minHeight: "50px",
    display: "flex",
    flexDirection: "row",
  };
  const helperText = {
    textAlign: "left",
    marginLeft: "14px",
    letterSpacing: "0.03333em",
    fontFamily: "Arial",
    color: "#d4323e",
    fontSize: "0.75rem",
  };

  return (
    <>
      <div style={divStyle}>
        <Typography variant="h5" style={labelStyle}>
          Title{" "}
        </Typography>
        <FormControl style={formStyle}>
          <TextField
            required
            id="title-recipe"
            label="Title"
            aria-label="title"
            type="text"
            variant="outlined"
            value={formData.title}
            onChange={(e) => {
              setFormData({
                ...formData,
                title: e.target.value,
              });
            }}
            helperText={
              titleError
                ? "This field is required"
                : "Max length: 30 characters"
            }
            error={titleError}
            inputProps={{ maxLength: 30 }}
          />
        </FormControl>
      </div>

      <div style={divStyle}>
        <Typography variant="h5" style={labelStyle}>
          Add a photo (optional)
        </Typography>
        {/* {displayIfImage()} */}
        <input
          accept="image/*"
          type="file"
          id="select-image"
          style={{ display: "none" }}
          onChange={(e) => setImage(e.target.files[0])}
        />
        <label htmlFor="select-image">
          <Button
            variant="outlined"
            color="primary"
            component="span"
            endIcon={<PhotoCamera />}
            style={buttonStyle}
          >
            {imageUrl ? "Change Image" : "Upload Image"}
          </Button>
        </label>
        {imageUrl && (
          <Box mt={2} textAlign="center">
            <div style={flexStyle}>Image Preview:</div>
            <div style={{ display: "flex" }}>
              <img
                style={flexStyle}
                src={imageUrl}
                alt="Preview"
                height="100px"
              />
              <IconButton
                sx={buttonStyle}
                aria-label="delete"
                onClick={() => removeImage()}
              >
                <DeleteIcon />
              </IconButton>
            </div>
          </Box>
        )}
        {selectedImage && imageUrl === null && <CircularProgress />}
      </div>

      <div style={divStyle}>
        <Typography variant="h5" style={labelStyle}>
          Description
        </Typography>
        <FormControl style={formStyle}>
          <TextField
            id="description-recipe"
            label="Description"
            aria-label="description"
            type="text"
            variant="outlined"
            multiline
            rows={3}
            onChange={(e) => {
              setFormData({
                ...formData,
                description: e.target.value,
              });
            }}
            value={formData.description}
          />
        </FormControl>
      </div>

      <div style={divStyle}>
        <FormControl required style={selectStyle}>
          <Typography variant="h5" style={labelStyle}>
            Servings
          </Typography>
          <div style={flexStyle}>
            <TextField
              required
              type="number"
              style={{ minWidth: "200px" }}
              onChange={(e) => {
                handleChangeServings(e);
              }}
              value={formData.servings}
              helperText={
                servingsError
                  ? "Please select a serving size greater than 0"
                  : ""
              }
              error={servingsError}
            />
            <Typography style={{ marginLeft: "10px" }}>serves</Typography>
          </div>
        </FormControl>
      </div>

      <div style={divStyle}>
        <FormControl required style={selectStyle}>
          <Typography variant="h5" style={labelStyle}>
            Difficulty
          </Typography>
          <div style={flexStyle}>
            {difficultyOptions.map((difficulty) => (
              <Button
                variant={
                  formData.difficulty === difficulty ? "contained" : "outlined"
                }
                style={{
                  marginRight: "30px",
                  minWidth: "100px",
                  minHeight: "50px",
                }}
                onClick={() => {
                  setFormData({
                    ...formData,
                    difficulty: difficulty,
                  });
                }}
                key={difficulty}
              >
                {difficulty}
              </Button>
            ))}
          </div>
          <Typography style={helperText}>
            {difficultyError ? "Please select a difficulty" : ""}
          </Typography>
        </FormControl>
      </div>

      <div style={divStyle}>
        <FormControl required style={formStyle}>
          <Typography variant="h5" style={labelStyle}>
            Utensils
          </Typography>
          <TagsInput
            fullWidth
            variant="outlined"
            id="tags"
            name="tags"
            placeholder="Add Utensils"
            formData={formData}
            setFormData={setFormData}
          />
        </FormControl>
      </div>

      <div style={divStyle}>
        <Typography variant="h5" style={labelStyle}>
          Prep Time
        </Typography>
        <div style={flexStyle}>
          <Select
            labelId="prepHours-select-label"
            id="prepHours-select"
            value={prepHours}
            label="prepHours"
            InputLabelProps={{ shrink: false }}
            onChange={(e) => {
              setPrepHours(e.target.value);
            }}
            style={timeStyle}
          >
            {hoursOptions.map((hour) => (
              <MenuItem value={hour}>{hour}</MenuItem>
            ))}
          </Select>
          <Typography style={{ marginLeft: "10px", marginRight: "40px" }}>
            hours{" "}
          </Typography>
          <Select
            labelId="prepMins-select-label"
            id="prepMins-select"
            value={prepMins}
            label="prepMins"
            InputLabelProps={{ shrink: false }}
            onChange={(e) => {
              setPrepMins(e.target.value);
            }}
            style={timeStyle}
          >
            {minsOptions.map((mins) => (
              <MenuItem value={mins}>{mins}</MenuItem>
            ))}
          </Select>
          <Typography style={{ marginLeft: "10px" }}>mins </Typography>
        </div>
      </div>

      <div style={divStyle}>
        <Typography variant="h5" style={labelStyle}>
          Cooking Time
        </Typography>
        <div style={flexStyle}>
          <Select
            labelId="cookHours-select-label"
            id="cookHours-select"
            value={cookHours}
            label="cookHours"
            InputLabelProps={{ shrink: false }}
            onChange={(e) => {
              setCookHours(e.target.value);
            }}
            style={timeStyle}
          >
            {hoursOptions.map((hour) => (
              <MenuItem value={hour}>{hour}</MenuItem>
            ))}
          </Select>
          <Typography style={{ marginLeft: "10px", marginRight: "40px" }}>
            hours{" "}
          </Typography>
          <Select
            labelId="cookMins-select-label"
            id="cookMins-select"
            value={cookMins}
            label="cookMins"
            InputLabelProps={{ shrink: false }}
            onChange={(e) => {
              setCookMins(e.target.value);
            }}
            style={timeStyle}
          >
            {minsOptions.map((mins) => (
              <MenuItem value={mins}>{mins}</MenuItem>
            ))}
          </Select>
          <Typography style={{ marginLeft: "10px" }}>mins </Typography>
        </div>
      </div>
    </>
  );
}
