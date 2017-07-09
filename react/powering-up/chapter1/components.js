class StoryBox extends React.Component {
    render() {
        var now = new Date()
        return (
            <div>
                <h3>Stories</h3>
                <p className="lead">
                    Current time: {now.toTimeString()}
                </p>
            </div>
        );
    }
}

ReactDOM.render(
    <StoryBox />, document.getElementById('story-app')
);
