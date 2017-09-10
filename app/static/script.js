/* Wang Editor */
var initial_editor = function(content_div='#content')
{
	if($(content_div).length>0){
		//hide the content div and create the editor div after the content div
		$(content_div).hide().after('<div id ="editor"></div>');
		//inital wang editor
		var e = window.wangEditor;
		var editor = new e('#editor');
		//Update onchange event for editor, copy the content from editor to to the content div
		editor.customConfig.onchange=function()
		{
			$(content_div).val(editor.txt.html());
		}
		editor.customConfig.lang={
			'设置标题':'Headings',
			'正文':'P',
			'文字颜色':'Color',
			'背景颜色':'Background',
			'链接文字': 'Link Text',
			'有序列表' : 'Numbers List',
			'无序列表' : 'Bullets  List',
			'设置列表' : 'Lists',
			'对齐方式':'Alignment',
			'靠左':'Align Left',
			'居中':'Center',
			'靠右':'Align Right',
			'表情':'Emoji',
			'手势':'Emoji - Hand',
			'图片链接': 'Image Link',
			'网络图片': 'Network Image',
			'插入视频': 'Insert Video',
			'格式如':'Example',
			'插入代码':'Insert Code',
			'插入表格':'Table',
			'创建':'Create',
			'行':'Row(s)',
			'列':'Column(s)',
			'的表格':'Table',
			'链接': 'Hyperlink'

		}
		editor.create();
		//copy the content from content div to editor div
		editor.txt.html($(content_div).val());
	}
}
