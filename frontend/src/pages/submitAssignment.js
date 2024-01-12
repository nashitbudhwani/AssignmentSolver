import React, { useState } from "react";
import axios from "axios";
import {
  Typography,
  Box,
  Paper,
  TextField,
  Button,
  Select,
  MenuItem,
} from "@mui/material";
import {
  faImage,
} from "@fortawesome/free-solid-svg-icons";
import Navbar from "../components/Navbar";
import UploadButton from "../components/UploadButton";

function CreatePost() {
  const [postId, setPostId] = useState("");
  const [content, setContent] = useState("");
  const [file, setFile] = useState(null);
  const [courseId, setCourseId] = useState("");
  const [title, setTitle] = useState("");

  const handlePostClick = async () => {
    try {

      // Call the second API to upload files using the postId obtained from the first API response
      if (file) {
        const formData = new FormData();
        formData.append("image", file);

        const uploadResponse = await axios.post(
          `https://dea5-117-102-52-3.ngrok-free.app/ocr`,
          {
            body:{
                formData,
            },
          }
        );

        return "Files uploaded successfully:"+ uploadResponse;
      }
    } catch (error) {
      console.error("Failed to create post or upload files!", error);
    }
  };


  return (
    <Box >

      <Box sx={{ p: 3, mt: "5vh" }}>
        <Typography
          sx={{
            color: "#000",
            fontFamily: "Montserrat",
            fontSize: "35px",
            fontStyle: "normal",
            fontWeight: "800",
            lineHeight: "normal",
          }}
        >
          Create a Post
        </Typography>
        <Paper
          sx={{
            my: 5,
            p: 3,
            backgroundColor: "white",
            borderRadius: "2",
            width: "95%",
            height: "450px",
            flexShrink: "0",
          }}
          elevation={1}
        >
          <Box>
            <UploadButton
              icon={faImage}
              onPostIdUpdate={setPostId}
              onFileSelect={setFile}
            />{" "}
          </Box>
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              marginTop: "10px",
            }}
          >
            <Button
              variant="contained"
              color="primary"
              onClick={handlePostClick}
            >
              Post
            </Button>
          </div>
        </Paper>
      </Box>
    </Box>
  );
}
export default CreatePost;
