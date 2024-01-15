import React, { useState } from "react";
import axios from "axios";
import { Typography, Box, Button } from "@mui/material";
import { faCloudArrowDown } from "@fortawesome/free-solid-svg-icons";
import UploadButton from "../components/UploadButton";
import Chat from "../pages/chat"; // Import your Chat component

function CreatePost() {
  const [postId, setPostId] = useState("");
  const [content, setContent] = useState("");
  const [file, setFile] = useState(null);
  const [isChatEnabled, setIsChatEnabled] = useState(false);
  const ocrApi = process.env.REACT_APP_API + "/ocr";
  console.log("ocrApi", ocrApi);
  const handlePostClick = async () => {
    try {
      if (!file) {
        console.log("No file selected");
        return;
      }

      const formData = new FormData();
      formData.append("image", file);

      const uploadResponse = await axios.post(ocrApi, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setContent(uploadResponse.data);
      console.log("Files uploaded successfully:", uploadResponse.data);
      setIsChatEnabled(true);
      return uploadResponse.data;
    } catch (error) {
      console.error("Failed to upload file!", error);
    }
  };

  return (
    <Box sx={{ mt: -5, pt: "0"}}>
      <Box sx={{ p: 3, mt: "5vh", backgroundColor: "#253439", mb:'500px'}}>
        <Typography
          sx={{
            my: "40px",
            color: "#fff",
            fontFamily: "Montserrat",
            fontSize: "35px",
            fontStyle: "normal",
            fontWeight: "800",
            lineHeight: "normal",
          }}
        >
          Assignment Solver by Ali Hassan and Nashit Budhwani
        </Typography>
        <Typography
          sx={{
            my: "20px",
            color: "#fff",
            fontFamily: "Montserrat",
            fontSize: "35px",
            fontStyle: "normal",
            fontWeight: "800",
            lineHeight: "normal",
          }}
        >
          Upload Your Assignment and Click post to get it solved
        </Typography>
        <Box>
          {isChatEnabled ? (
            <Chat answer={content} />
          ) : (
            <UploadButton
              icon={faCloudArrowDown}
              onPostIdUpdate={setPostId}
              onFileSelect={setFile}
            />
          )}
        </Box>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginTop: "10px",
          }}
        >
          {!isChatEnabled && (
            <Button
              variant="contained"
              color="primary"
              onClick={handlePostClick}
            >
              Post
            </Button>
          )}
        </div>
      </Box>
    </Box>
  );
}

export default CreatePost;
