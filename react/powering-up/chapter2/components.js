class Comment extends React.Component {
    render() {
        return(
            <div className="comment">
                <p className="comment-header">Anne Droid</p>
                <p className="comment-body">
                    I wanna know what love is...
                </p>
                <div className="comment-footer">
                    <a href="#" className="comment-footer-delete">
                        Delete Comment
                    </a>
                </div>
            </div>
        );
    }
}

class CommentBox extends React.Component {
    render(){
        return(
            <div className="comment-box">
                <h3>Comments</h3>
                <h4 className="comment-count">2 comments</h4>
                <div className="comment-list">
                    <Comment />
                    <Comment />
                </div>
            </div>
        );
    }
}

ReactDOM.render(
    <CommentBox />, document.getElementById('comment-box')
);

