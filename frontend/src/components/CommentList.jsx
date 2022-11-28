import React from "react";
import {
  Box,
  Avatar,
  Typography,
  Divider,
  Rating,
  Tooltip,
  IconButton,
  CircularProgress,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Button,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import defaultPic from "../images/remy.jpg";
import fetchData from "../helper.js";

export default function CommentsList({
  comments,
  setUpdateComments,
  updateComments,
}) {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  const [user, setUser] = React.useState(null);
  const [loading, setLoading] = React.useState(true);

  const [openEdit, setOpenEdit] = React.useState(false);
  const [editedComment, setEditedComment] = React.useState("");
  const [editedRating, setEditedRating] = React.useState(0);
  const [editedId, setEditedId] = React.useState(null);

  const [picHover, setPicHover] = React.useState(false);

  async function loadU() {
    const data = await fetchData("GET", `api/user_details`, {}, token);
    return data;
  }

  React.useEffect(() => {
    async function loadUser() {
      if (token) {
        const userInfo = await loadU();
        setUser(userInfo);
      }
      setLoading(false);
    }
    loadUser();
  }, []);

  const editComment = () => {
    // post the edited comment
    console.log(editedRating);
    fetchData(
      "PUT",
      `api/${comments[0].recipeId}/comment`,
      {
        token: token,
        comment: editedComment,
        rating: editedRating,
        commentId: editedId,
      },
      token
    );
    setOpenEdit(false);
    setUpdateComments(!updateComments);
  };

  const deleteComment = (commentId) => {
    fetchData(
      "DELETE",
      `api/${comments[0].recipeId}/comment`,
      { token: token, commentId: commentId, comment: "" },
      null
    );
    setUpdateComments(!updateComments);
  };

  const avatarStyle = { margin: "20px", width: "60px", height: "60px" };
  const avatarHoverStyle = {
    cursor: "pointer",
    margin: "20px",
    width: "60px",
    height: "60px",
  };
  const flexStyle = { display: "flex", padding: "10px 0px" };
  const commentBoxStyle = { padding: "20px" };
  const ratingStyle = { marginLeft: "10px", marginTop: "-2px" };
  const commentInputStyle = { marginTop: "10px" };

  return (
    <>
      {loading ? (
        <Box sx={{ display: "flex" }}>
          <CircularProgress />
        </Box>
      ) : (
        <Box>
          {comments.map((comment, index) => {
            return (
              <>
                <Divider />
                <Box style={flexStyle}>
                  {comment.profilePic ? (
                    <Avatar
                      style={picHover ? avatarHoverStyle : avatarStyle}
                      alt="user's profile picture"
                      onMouseEnter={() => setPicHover(true)}
                      onMouseLeave={() => setPicHover(false)}
                      onClick={() => navigate(`/profile/${comment.userId}`)}
                      src={comment.profilePic}
                    />
                  ) : (
                    <Avatar
                      style={picHover ? avatarHoverStyle : avatarStyle}
                      alt="user's profile picture"
                      onMouseEnter={() => setPicHover(true)}
                      onMouseLeave={() => setPicHover(false)}
                      onClick={() => navigate(`/profile/${comment.userId}`)}
                      src={defaultPic}
                    />
                  )}
                  <Box style={commentBoxStyle}>
                    <Typography
                      variant="body2"
                      onClick={() => navigate(`/profile/${comment.userId}`)}
                    >
                      @ {comment.username}
                    </Typography>
                    <Typography variant="body1">{comment.comment}</Typography>
                    {comment.rating && (
                      <Box style={flexStyle}>
                        <Divider light />
                        <Typography variant="body2">Rating: </Typography>
                        <Rating
                          style={ratingStyle}
                          defaultValue={comment.rating}
                          precision={0.5}
                          readOnly
                        />
                      </Box>
                    )}
                    {token && comment.userId === user.id && (
                      <Box>
                        <Tooltip title="Edit Comment">
                          <IconButton>
                            <EditIcon
                              onClick={() => {
                                setOpenEdit(true);
                                setEditedComment(comment.comment);
                                setEditedRating(comment.rating);
                                setEditedId(comment.id);
                              }}
                            />
                          </IconButton>
                        </Tooltip>

                        <Tooltip title="Delete Comment">
                          <IconButton>
                            <DeleteIcon
                              onClick={() => {
                                deleteComment(comment.id);
                              }}
                            />
                          </IconButton>
                        </Tooltip>
                      </Box>
                    )}
                  </Box>
                </Box>
              </>
            );
          })}

          <Dialog
            open={openEdit}
            onClose={() => setOpenEdit(false)}
            aria-labelledby="edit-comments-dialog"
            aria-describedby="edit-comments-dialog"
            fullWidth
            maxWidth="md"
          >
            <DialogTitle>Edit Comment</DialogTitle>
            <DialogContent>
              <TextField
                fullWidth
                label="Edit Your Comment"
                style={commentInputStyle}
                value={editedComment}
                onChange={(e) => setEditedComment(e.target.value)}
              />
              <Rating
                style={commentInputStyle}
                size="large"
                precision={0.5}
                value={editedRating}
                onChange={(e, newValue) => {
                  setEditedRating(newValue);
                }}
              />
            </DialogContent>
            <DialogActions>
              <Button variant="contained" onClick={editComment}>
                Edit Comment
              </Button>
            </DialogActions>
          </Dialog>
        </Box>
      )}
    </>
  );
}
