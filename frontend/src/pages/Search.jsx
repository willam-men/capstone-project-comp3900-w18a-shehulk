import React from "react";
import {
  Paper,
  Typography,
  TextField,
  Box,
  Button,
  InputAdornment,
} from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import { useNavigate } from "react-router-dom";

import AdvancedSearch from "../components/AdvancedSearch";

export default function Search() {
  const navigate = useNavigate();
  const [isAdvSearch, setIsAdvSearch] = React.useState(false);
  const [title, setTitle] = React.useState("");

  const openAdvSearch = () => {
    setIsAdvSearch(!isAdvSearch);
  };

  const submitSimpleSearch = () => {
    navigate(`/search/title=${title}`);
  };

  const paperStyle = { padding: "100px", width: "70vw", margin: "50px auto" };
  const searchLabel = { padding: "10px", marginRight: "20px" };
  const inputStyle = { width: "100%" };
  const advContainer = { padding: "30px 0px" };
  const advSearch = { padding: "10px", marginRight: "20px", marginTop: "30px" };

  return (
    <>
      <Paper elevation={3} style={paperStyle}>
        <Box sx={{ display: "flex" }}>
          <Typography variant="h5" style={searchLabel}>
            Search
          </Typography>
          <TextField
            style={inputStyle}
            label="By Title"
            variant="outlined"
            onChange={(e) => setTitle(e.target.value)}
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <SearchIcon />
                </InputAdornment>
              ),
            }}
          />
        </Box>
        <Button
          style={advSearch}
          sx={{ display: "flex" }}
          onClick={openAdvSearch}
        >
          {isAdvSearch ? "Simple Search" : "Advanced Search"}
        </Button>

        {isAdvSearch ? (
          <Box style={advContainer}>
            <AdvancedSearch title={title} />
          </Box>
        ) : (
          <Box>
            <Button variant="contained" onClick={submitSimpleSearch}>
              Submit
            </Button>
          </Box>
        )}
      </Paper>
    </>
  );
}
